<<<<<<< HEAD
from app import db,LoginManager
from datetime import datetime
from flask_login import UserMixin # qual modelo 


@LoginManager.user_loader
#carregar o usuario no login
def load(user_id):
    return User.query.get(user_id)


class User(db.Model,UserMixin):
    __tablename__= "user"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nome = db.Column(db.String(100), nullable=True)
    sobrenome = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    senha = db.Column(db.String(100), nullable=True)

=======
from app import db
from datetime import datetime
>>>>>>> 7f8a86282e522ad4c689a07a6ae339ea72ca01b9
class Produto(db.Model):    
    __tablename__= "produto"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    quantidade=db.Column(db.Integer, nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    fornecedor = db.Column(db.String(100), nullable=False)
    descricao= db.Column(db.String(500),nullable=False)
    data_de_fabricacao= db.Column(db.DateTime,nullable=False)
    data_de_validade = db.Column(db.DateTime,nullable=False)
<<<<<<< HEAD




=======
>>>>>>> 7f8a86282e522ad4c689a07a6ae339ea72ca01b9
