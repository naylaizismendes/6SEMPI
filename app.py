from flask import Flask
from routes.home import home_route
from flask_bootstrap import Bootstrap

app = Flask(__name__)

# Inicializando o Bootstrap5 no Flask
bootstrap = Bootstrap(app)

# Registrando a blueprint
app.register_blueprint(home_route)

# Iniciando o servidor
if __name__ == '__main__':
    app.run(debug=True)
