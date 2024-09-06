from flask import Flask,render_template
#CRIAÇÃO DAS ROTAS(AS REQUISIÇÃO)

#inicializando uma açao
app= Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

#execucao MODO DESENVOLVEDOR
app.run(debug=True)