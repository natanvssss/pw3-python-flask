from flask import render_template, request, redirect, url_for


def init_app(app):
    listaFilmes =[{'filme': 'Star Wars', 'tipo': 'Ficçao','duracao': '2h'}]


    @app.route('/')
    def home():
        return render_template('index.html')


    @app.route('/formulario')
    def form():
        return render_template('formulario.html')
    
    @app.route('/cadfilmes',methods=['GET','POST'])
    def cadfilmes():
        if request.method == 'POST':
            listaFilmes.append({'filme': request.form.get('filme'), 'tipo' : request.form.get('tipo'), 'duracao' : request.form.get('duracao')})
            return redirect(url_for('lista'))
        return render_template('cadfilmes.html')


        
    @app.route('/lista',methods=['GET','POST'])
    def lista():
        return render_template('lista.html',
                                 listaFilmes=listaFilmes)        
        
    @app.route('/cadgames', methods=['GET','POST'])
    def cadgames():
        if request.method ==  'POST':
            listaFilmes.append({'Filme': request.form.get('Filme'), 'Tipo': request.form.get('Tipo'),   'Duração' : request.form.get('Duração')})
            return render_template('cadfilmes.html',
                                   listaFilmes = listaFilmes)    
  
        
