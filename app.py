from flask import Flask, template_rendered,request

app = Flask(__name__)

#rota para a pagina inicial da aplicação
@app.route('/')
def index():
    return "residente evil 4 é o melhor remake"

