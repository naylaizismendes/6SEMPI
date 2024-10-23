from flask import Flask
from flask_bootstrap import Bootstrap

# Importando as rotas da pasta routes
from routes.home import home_route  # Rota para home.py
from routes.login import login_route  # Rota para login.py
from routes.cadastrar import cadastrar_route  # Rota para cadastrar.py
#importando bobilioteca de banco de dados
from flask_sqlalchemy import SQLAlchemy
from models.produto import db

app=Flask(__name__)
db.init_app(app)
#uri conexao com o banco de dados 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///produto.db"

db= SQLAlchemy(app)
bootstrap = Bootstrap(app)




 
    




# Registrando as Blueprints
app.register_blueprint(home_route)  # Rota para home.py
app.register_blueprint(login_route)  # Rota para login.py
app.register_blueprint(cadastrar_route)  # Rota para cadastrar.py


#inicializar o banco de dados -> sql lite 
with app.app_context():
    db.create_all()

#inicizializando o sistema 
if __name__ == '__main__':
    
    db.create_all()   
    app.run(debug=True)
