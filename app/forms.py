from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired
#tabelas dos bancos de dados
class LoginForm(FlaskForm):
    username=StringField("username",validators=[DataRequired("Username")]) #
    password =PasswordField("Password",validators=[DataRequired("Passworld")])#
    remember_me=BooleanField("remember_me",validators=[DataRequired("Remember me")])# NOM(
        