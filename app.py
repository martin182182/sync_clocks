from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from flask.json import jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def welcome():
    return "<p>Hola</p>"

@app.route("/sync", methods=['POST'])
def syncClock():
    timeServer = datetime.now()
    formmatted = request.get_json()
    timeClient = datetime.strptime(formmatted['key'],"%Y-%m-%dT%H:%M:%S.%f")
    dif = timeServer - timeClient
    res = (dif.days * 24 * 3600 + dif.seconds)/60
    res = res/2
    timeServer = timeServer + timedelta(minutes=res)
    dif = timeServer - timeClient
    res = (dif.days * 24 * 3600 + dif.seconds)/60
    timeClient = timeClient + timedelta(minutes=res)
    print(timeServer.time())
    print(timeClient.time())
    return 'Sincronizado'


