from flask import flask

app = flask(__name__)

@app.route('/')
def index():
    return '<h1>Saya Samad</h1>'