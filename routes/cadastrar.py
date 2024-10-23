from flask import Blueprint,render_template
from models.produto import Produto, db 
#foi criada blueprintsn "home(principal)"
cadastrar_route = Blueprint('cadastrar',__name__)
#isso aqui significa uma rota-acesso - HOME PAGE(PAGINA PRINCP)
@cadastrar_route.route('/cadastrar')
def cadastrar():
    return render_template('cadastar.html')

