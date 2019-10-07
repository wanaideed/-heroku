# from flask import flask

# app = flask(__name__)

# @app.route('/')
# def index():
#     return '<h1>Saya Samad</h1>'
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>M</h1>'
