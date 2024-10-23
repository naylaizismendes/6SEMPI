#biblioteca orm
from flask_sqlalchemy import SQLAlchemy

#criaçao da modelo ->tabela PRODUTO!
db=  SQLAlchemy()

class Produto(db.Model):    
    __tablename__= "produto"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    quantidade=db.Column(db.number, nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    fornecedor = db.Column(db.String(100), nullable=False)
    descricao= db.Column(db.String(500),nullable=False)
    data_de_fabricacao= db.Column(db.Date,nullable=False)
    data_de_validade = db.Column(db.Date,nullable=False)