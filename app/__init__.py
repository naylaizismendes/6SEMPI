from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap4
app= Flask(__name__)
bootstrap = Bootstrap4(app)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db' #nome do banco de dados 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY']= 'AAAAAA-AAAAAAA'
#DEFINIR A VARIAVEL DO BANCO DE DADOS
db=SQLAlchemy(app)
migrate=Migrate(app,db)

from app.routes import homepage 
from app.routes import cadastrar_novo


# tela principal(MENU) 
from app.models import Produto
                                #exibir produto