from flask import Flask
from flask import request

from wordladder import WordLadder
import json

app = Flask(__name__)

@app.route("/")
def word_ladder():
    start = request.args.get('start', default = '', type = str)
    target = request.args.get('target', default = '', type = str)
    dictionary = request.args.get('dic', default = '', type = str).split(",")    

    result = WordLadder().shortest_path(start, target, dictionary)
    return json.dumps(result.path)