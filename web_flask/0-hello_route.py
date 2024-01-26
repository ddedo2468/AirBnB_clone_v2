#!/usr/bin/python3
""" starting my first page of Flask app """

from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    """returns hello HBNB!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(port=5000, host='0.0.0.0')
