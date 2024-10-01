#IMPORTANTO AS PASTAS,BIBLIOTECAS E TEMPLATES
from flask import Flask


from routes.home import home_route
from routes.login import login_route


from flask_bootstrap import Bootstrap


#importando - models
from app import LoginForm

app = Flask(__name__)

# Inicializando o Bootstrap5 no Flask
bootstrap = Bootstrap(app)


# Registros das blueprint HOME _> home.py
app.register_blueprint(home_route)


# Registrando o Blueprint LOGIN -> login.py
app.register_blueprint(login_route)
# Iniciando o servidor
if __name__ == '__main__':
    app.run(debug=True)
 
 
 
 #rotas cridas para acessar os conteudos da pagee 
 #home/.../...