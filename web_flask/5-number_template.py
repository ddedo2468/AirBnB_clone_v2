#!/usr/bin/python3
""" first hbnb page """

from flask import Flask, render_template, render_template_string
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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text='is cool'):
    """ python page """
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>")
def isNum(n):
    """ is a number """
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def numberTemplate(n):
    """ is a number and template"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(port=5000, host='0.0.0.0')
