from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import DataRequired, Lenght, Email, EqualTo 

class formLogin(FlaskForm):
    email = StringField("email" ,validators=[DataRequired()])
    senha = PasswordField("senha", validators=[DataRequired(),Lenght(6, 12)]) 
    submitilogin = SubmitField("login")

class formNovoUsuario(FlaskForm):
    nome = StringField( 'nome', validators=[DataRequired()])
    Email = StringField("email", validators=[DataRequired(),Email()])
    celular = StringField("celular", validators=[])
    cpf = StringField("CPF", validators=[])
    senha = PasswordField('Senha', validators=[DataRequired(),Lenght(6, 12)])
    senhaConfirmacao = PasswordField("Confirmacao de Senha", validators=[DataRequired(),EqualTo('senha')])
    submit = SubmitField("Criar conta")


