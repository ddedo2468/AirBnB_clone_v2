#!/usr/bin/python3
""" first hbnb page """

from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    """ hello HBNB """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ HBNB """
    return "HBNB"


@app.route("/c/<text>")
def cFun(text):
    """ c page """
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(port=5000, host='0.0.0.0')
