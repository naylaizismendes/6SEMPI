from app import app, db
from flask import render_template, url_for, request
from app.models import Produto
from app.forms import ProdutoForm
from datetime import datetime 

# Homepage
@app.route('/')
def homepage():
    return render_template('base.html')

# Rota para cadastrar novos produtos
@app.route('/produtos/', methods=['GET', 'POST'])
def cadastrar_novo():
    form = ProdutoForm()
    context = {}
    if request.method == 'POST':
        nome = request.form.get('nome')
        quantidade = request.form.get('quantidade')
        categoria = request.form.get('categoria')
        fornecedor = request.form.get('fornecedor')
        descricao = request.form.get('descricao')
        data_de_fabricacao = request.form.get('data_de_fabricacao')
        data_de_validade = request.form.get('data_de_validade')

        # Convertendo strings de data para objetos datetime
        data_de_fabricacao = datetime.strptime(data_de_fabricacao, '%Y-%m-%d')
        data_de_validade = datetime.strptime(data_de_validade, '%Y-%m-%d')

        produto = Produto(
            nome=nome,
            quantidade=quantidade,
            categoria=categoria,
            fornecedor=fornecedor,
            descricao=descricao,
            data_de_fabricacao=data_de_fabricacao,
            data_de_validade=data_de_validade
        )
        db.session.add(produto)
        db.session.commit()
 
    return render_template('produto.html', context=context, form=form)

# Rota para listar produtos no estoque
@app.route('/estoque/lista/')
def estoque_lista():
    pesquisa = request.args.get('pesquisa', '')
    dados = Produto.query.order_by('nome')
    
    if pesquisa:
        dados = dados.filter_by(nome=pesquisa)

    context = {'dados': dados.all()}

    for linha in dados:
        print(linha.nome)
        print(linha.quantidade)
        print(linha.fornecedor)
        print(linha.descricao)
        print(linha.data_de_fabricacao)
        print(linha.data_de_validade)

    return render_template('estoque.html', context=context)

@app.route('/produto/<int:id>/')
def produtoDetail(id):
    obj = Produto.query.get(id) #recupera o objeto 
    

    return render_template('produto_detail.html', obj=obj)