import flask
from flask import render_template
from flask import request

import common

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/pownal-solar', methods=['POST'])
def toggleRelay():
    relayNum = request.args.get('relayNum')
    common.toggleRelay(int(relayNum))
    return ''

app.run(host='0.0.0.0')
