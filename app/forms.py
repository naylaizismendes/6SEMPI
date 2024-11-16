
from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,DateField,FloatField,IntegerField,SubmitField,TextAreaField,EmailField
from app.models import Produto


class ProdutoForm(FlaskForm):
    nome = StringField( 'nome',validators=()) #vALIDATORS = QUTD MAXIA
    quantidade=IntegerField('quantidade',validators=())
    categoria = categoria = SelectField(
    'Categoria',
    choices=[
        ('geral', 'Geral'),
        ('mercearia', 'Mercearia'),
        ('frios', 'Frios'),
        ('congelados', 'Congelados'),
        ('limpeza', 'Limpeza')
    ],
    validators=[]
)
    
    fornecedor = StringField('fornecedor',validators=())
    descricao= descricao = TextAreaField('Descrição', validators=[])
    data_de_fabricacao= DateField('data_de_fabricacao',validators=())
    data_de_validade = DateField('data_de_validade',validators=())
    btnSubmit=SubmitField(' Cadastrar',validators=())


    def save(self):
        produto=Produto(
            nome=self.data,
            quantidade=self.data,
            categoria=self.data ,
            fornecedor=self.data,
            descricao=self.data ,
            data_de_fabricacao=self.data,
            data_de_validade=self.data,

        )