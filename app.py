from flask import Flask, render_template

app = Flask(__name__)

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

#rota para login
@app.route('/login')
def login():
    return render_template('login.html')

#rota para ead
@app.route('/sobre_ead')
def sobre_o_ead():
    return render_template('sobre_ead.html')

if __name__== '__main__':
    app.run(debug=True)
    
