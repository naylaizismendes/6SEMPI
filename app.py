from flask import Flask,render_template
from flask_bootstrap import Bootstrap4


app = Flask(__name__)

bootstrap = Bootstrap4(app)
#CRIAÇÃO DAS ROTAS(AS REQUISIÇÃO)

#inicializando uma açao declarando os arqivos
@app.route("/")
@app.route("/index")
def create_app():
    app= Flask(__name__ ,
           isinstance_relative_config=True,
           static_folder='static',
           template_folder='templates')



def create_app():
    titulo= "Sistema de estoque"
    products= Product.query.all()                         
    #vari.contexto  valor
    return render_template("index.html",titulo=titulo ,products=products,title="Pagina Principal")

#execucao MODO DESENVOLVEDOR
app.run(debug=True)