
from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import StringField,SelectField,DateField,FloatField,IntegerField,SubmitField,TextAreaField,EmailField,PasswordField
from app.models import Produto,User
from wtforms.validators import DataRequired,Email,ValidationError,EqualTo
from app import db, bcrypt

class UserForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), EqualTo('confirmacao_senha', message='As senhas devem coincidir')])
    confirmacao_senha = PasswordField('Confirmação de Senha', validators=[DataRequired()])

    btnSubmit=SubmitField('Cadastrar')

    def validade_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Usuário já cadastrado')

    def save(self):
        senha=bcrypt.generate_password_hash(self.senha.data.encode('utf-8'))
        user=User( 
            nome = self.nome.data,
            sobrenome=self.sobrenome.data,
            email =self.email.data,
            senha =senha
        )

        db.session.add(user)
        db.session.commit()
        return user



class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    btnSubmit = SubmitField('Login')

    def login(self):
        user = User.query.filter_by(email=self.email.data).first()
        if user and bcrypt.check_password_hash(user.senha, self.senha.data.encode('utf-8')):
            return user
        elif not user:
            raise Exception('Usuário não encontrado')
        else:
            raise Exception('Senha incorreta')

    

   
=======
from wtforms import StringField,SelectField,DateField,FloatField,IntegerField,SubmitField,TextAreaField,EmailField
from app.models import Produto

>>>>>>> 7f8a86282e522ad4c689a07a6ae339ea72ca01b9

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