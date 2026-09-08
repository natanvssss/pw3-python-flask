import json
import urllib.request

from flask import render_template


def fetch_json(url):
    request = urllib.request.Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode('utf-8'))


def build_pokemon_summary(pokemon):
    sprite = (
        pokemon.get('sprites', {}).get('other', {}).get('official-artwork', {}).get('front_default')
        or pokemon.get('sprites', {}).get('front_default')
    )

    return {
        'id': pokemon['id'],
        'name': pokemon['name'].capitalize(),
        'slug': pokemon['name'],
        'image': sprite,
        'types': [tipo['type']['name'] for tipo in pokemon.get('types', [])],
        'height': round(pokemon['height'] / 10, 1),
        'weight': round(pokemon['weight'] / 10, 1),
    }


def init_app(app):
    @app.route('/')
    def home():
        pokedex = []
        data = fetch_json('https://pokeapi.co/api/v2/pokemon?limit=200&offset=0')

        for item in data.get('results', []):
            pokemon = fetch_json(item['url'])
            pokedex.append(build_pokemon_summary(pokemon))

        return render_template('index.html', pokemons=pokedex)

    @app.route('/pokemon/<string:pokemon_name>')
    def pokemon_detail(pokemon_name):
        pokemons = fetch_json(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}')
        summary = build_pokemon_summary(pokemons)

        species = fetch_json(pokemons['species']['url'])
        descriptions = species.get('flavor_text_entries', [])
        description = 'Descrição indisponível no momento.'

        for entry in descriptions:
            if entry.get('language', {}).get('name') == 'en':
                description = entry.get('flavor_text', description).replace('\n', ' ')
                break

        evolution_url = species.get('evolution_chain', {}).get('url')
        evolution_chain = []

        if evolution_url:
            chain_data = fetch_json(evolution_url)

            def collect(node):
                evolution_chain.append(node['species']['name'])
                for child in node.get('evolves_to', []):
                    collect(child)

            collect(chain_data.get('chain', {}))

        return render_template(
            'pokemon_detail.html',
            pokemon=summary,
            description=description,
            stats=pokemons.get('stats', []),
            evolution=evolution_chain,
        )

