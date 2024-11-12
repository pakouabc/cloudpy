from flask import Flask

app = Flask(__name__)

@app.route("/")
def casa():
    return "<p>Saludos desde casa</p>"

@app.route("/about")
def sobredemi():
    return "Hola soy pako"