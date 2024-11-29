from app import app, db

from flask import render_template, url_for, request,redirect,flash
from app.models import Produto,User
from app.forms import ProdutoForm,UserForm,LoginForm
from datetime import datetime 
from flask_login import login_user, logout_user,current_user #verificaçao de usuario acesso , logout ,verificar no sistema
# Homepage
@app.route('/',methods=['GET','POST'])
def homepage():
    form =LoginForm()
    
    if form.validate_on_submit():
        user = form.login()
        login_user(user,remember=True)
    return render_template('index.html',form=form)
 
 #cadastrar usuario 
@app.route('/cadastrando_usuario/',methods=['GET','POST'])
def cadastro():
    form=UserForm()
    if form.validate_on_submit():
        user= form.save()
        login_user(user,remember=True)
        return redirect(url_for('homepage'))
    return render_template('cadastro.html', form=form)


@app.route('/sair/')
def logout():
    logout_user()
    return redirect(url_for('homepage'))


from flask import render_template, url_for, request
from app.models import Produto
from app.forms import ProdutoForm
from datetime import datetime 

# Homepage
@app.route('/')
def homepage():
    return render_template('index.html')


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

@app.route('/produto/<int:id>/', methods=["get",'post'])
def produtoDetail(id):
    obj = Produto.query.get(id) #recupera o objeto 
    
    if not Produto:
        flash('produto não encontrado!!!')
        return redirect(url_for('estoque__lista'))

    if request.method == 'POST':
        nome = request.form.get('nome')
        quantidade = request.form.get('quantidade')
        categoria = request.form.get('categoria')
        fornecedor = request.form.get('fornecedor')
        descricao = request.form.get('descricao')
        data_de_fabricacao = request.form.get('data_de_fabricacao')
        data_de_validade = request.form.get('data_de_validade')

        produto=Produto.query.all()
        flash('Produto atualizado com sucesso')
        return redirect(url_for("estoque_lista"))
    return render_template('produto_detail.html', obj=Produto)



@app.route('/produto/<int:id>/')
def produtoDetail(id):
    obj = Produto.query.get(id) #recupera o objeto 
    

    return render_template('produto_detail.html', obj=obj)

