from flask import Flask, template_rendered,request

app = Flask(__name__)

@app.route('/')
def index():
    return "residente evil 4 é o melhor remake"

if __name__ == '__main__':
    app.run(debug=True)
        