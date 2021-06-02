import re
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books= [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'year_published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'year_published': '1975'}  
]

@app.route('/',methods=['GET'])
def home():
    return " <h1>Dudinha ta ensinando nós</h1> <p>Vasco é sempre vice do meu Mengo!</p>"

@app.route('/api/v1/resources/books/all',methods=['GET'])
def api_all():
    return jsonify(books)
#@app.route('/titulo',methods=['GET'])
#def numeros():
#    return "<h1> Flamengo tem 30 titulos</h1>"

@app.route('/api/v1/resources/books',methods=['GET'])
def id_all():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Erro, id não encontrado"

    results = []
    for book in books:
        if book['id'] == id:
            results.append(book)
    return jsonify(results)


@app.route('/api/v1/resources/books/year/',methods=['GET'])
def year_all():
    if 'year_published' in request.args:
        year = request.args['year_published']
    else:
        return "Erro, Ano não encontrado"
    results = []
    for book in books:
        if book['year_published'] == year:
            results.append(book)
    return jsonify(results)

app.run()