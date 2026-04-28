# importando o FLASK-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# CArregando o SLQAlchemy em uma variável
db = SQLAlchemy()

# Criando uma classe para representar a entidade games no banco


class Game(db.Model):
    # Definindo os atributos (columas) da tabela
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    plataforma = db.Column(db.String(150))
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)

    # Inciando as variáveis na classe(Método Construtor)
    def _init_(self, titulo, ano, categoria, plataforma, preco, quantidade):
        self.titulo = titulo
        self.ano = ano
        self.categoria = categoria
        self.plataforma = plataforma
        self.preco = preco
        self.quantidade = quantidade
