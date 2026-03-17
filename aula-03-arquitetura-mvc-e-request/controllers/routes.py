# Importando o flask para a aplicação
from flask import render_template, request
# Criando a função principal para a inicializar as rotas


def init_app(app):
    # Criando a rota principal do site
    @app.route('/')
    # def cria funções no python
    def home():
        return render_template('index.html')

    @app.route('/games')
    def games():
        # criando variáveis para a rota de games
        titulo = "Portal 2"
        ano = 2011
        categoria = "Puzzle"
        # Lista de Jogadores(uma lista é um vetor/array)
        jogadores = ['Marcos', 'Richard', 'Miguel', 'Renato', 'Pedro']

        # Enviando categorias para html
        return render_template('games.html',
                               titulo=titulo,
                               ano=ano,
                               categoria=categoria,
                               jogadores=jogadores)

    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():
        # Criando um objeto
        console = {"Nome": "Playstation 2",
                   "Fabricante": "Sony",
                   "Ano": 2000}
        listaConsoles = ['Playstation 5', 'Xbox One',
                         'Super Nintendo', 'Atari', '3DS']
        # Recebendo o valor do formulário
        if request.method == 'POST':
            if request.form.get('novoConsole'):
                listaConsoles.append(request.form.get('novoConsole'))

        return render_template('consoles.html',
                               console=console,
                               listaConsoles=listaConsoles)
