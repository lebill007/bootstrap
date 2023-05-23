from flask import Flask, render_template
from forms import formLogin, formNovoUsuario 

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a271f94d24f9261c5cd19428c513c297'

#rota para a pagina inicial da aplicação
@app.route('/')
def index():
    return render_template("index.html")

#rota para contato
@app.route("/contato")
def contato():
    return render_template('contato.html')

#rota para cursos
@app.route('/cursos')
def cursos():
    return render_template("cursos.html")



#rota para ead
@app.route('/sobre_ead')
def sobre_o_ead():
    return render_template('sobre_ead.html')

 #enviando informações para o arquivo html(Templates)
 @app.route('/login', methods=["get","post"])
 def login():
    titulo = "login de acesso"
    descricao = "Formulário de login"

    form_login = formLogin()
    form_novo_usuario = formNovoUsuario()

    return render_template('loginObjeto.html', titulo=titulo, descricao=descricao, form_login=form_login, form_novo_usuario=form_novo_usuario)


  

if __name__== '__main__':
    app.run(debug=True)
    
