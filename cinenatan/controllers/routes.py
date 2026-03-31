from flask import render_template, request


def init_app(app):
    listaFilmes =[{'filme': 'Star Wars', 'tipo': 'Ficçao','duração': '2h'}]


    @app.route('/')
    def home():
        return render_template('index.html')


    @app.route('/formulario')
    def form():
        nome = nome
        email = email
        senha = senha
        return render_template('formulario.html')
    
    @app.route('/cadfilmes')
    def cad():
        filme=filme
        tipo = tipo
        duracao = duracao
        return render_template('cadfilmes.html')


        
    @app.route('/lista',methods=['GET','POST'])
    def filmes():
        filme = {"Filme":"Star Wars",
                 "Tipo": "Ficção",
                 "Duração": "2h11"}
        if request.method == 'POST':
            if request.form.get('novoFilme'):
                listaFilmes.append(request.form.get('novoFilme'))
        return render_template('lista.html',
                               filme=filme,
                               listaFilmes=listaFilmes)        
        
    @app.route('/cadgames', methods=['GET','POST'])
    def cadgames():
        if request.method ==  'POST':
            listaFilmes.append({'Filme': request.form.get('Filme'), 'Tipo': request.form.get('Tipo'),   'Duração' : request.form.get('Duração')})
            return render_template('cadfilmes.html',
                                   listaFilmes = listaFilmes)    
  
        
