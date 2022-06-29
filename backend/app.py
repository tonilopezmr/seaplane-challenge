from flask import Flask
from flask import request

from wordladder import WordLadder
import json

app = Flask(__name__)

@app.route("/")
def word_ladder():
    start = request.args.get('start', default = '', type = str)

    if start == '':
        return json.dumps({'error': 'start parameter is missing'})

    target = request.args.get('target', default = '', type = str)

    if target == '':
        return json.dumps({'error': 'target parameter is missing'})

    dictionary = request.args.get('dic', default = '', type = str).split(",")    
    
    if dictionary == ['']:
        return json.dumps({'error': 'dictionary parameter is missing'})


    result = WordLadder().shortest_path(start, target, dictionary)
    return json.dumps(result.path)