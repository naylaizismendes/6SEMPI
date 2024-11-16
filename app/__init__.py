from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap4
from flask_login
from flask_bcrypt
#atualizando a camada de segurança
import os #icarregar a var
from dotenv import load_dotenv
load_dotenv('.env')

app= Flask(__name__)
bootstrap = Bootstrap4(app)


#atualizando a camada de segurança
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URI') #nome do banco de dados 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY']= os.getenv('SECRET_KEY')
#DEFINIR A VARIAVEL DO BANCO DE DADOS
db=SQLAlchemy(app)
migrate=Migrate(app,db)

from app.routes import homepage 
from app.routes import cadastrar_novo
from app.routes import produtoDetail

# tela principal(MENU) 
from app.models import Produto
                                #exibir produto