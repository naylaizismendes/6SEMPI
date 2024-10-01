#iportando o framework - leitura dos templates -
from flask import Flask, Blueprint, render_template
from app import LoginForm


app = Flask(__name__)

# Criando um Blueprint - DO LOGIN
login_route = Blueprint('login', __name__)

# Usando o método .route() para definir rotas
@app.route.route("login")
def login():
    form =LoginForm()
    return render_template('login.html',form=form)
# chamando a app...


if __name__ == "__main__":
    app.run()
