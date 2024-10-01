from flask import Blueprint,render_template
#foi criada blueprintsn "home(principal)"
home_route = Blueprint('home',__name__)
#isso aqui significa uma rota-acesso - HOME PAGE(PAGINA PRINCP)
@home_route.route('/')
def home():
    return render_template('base.html')

