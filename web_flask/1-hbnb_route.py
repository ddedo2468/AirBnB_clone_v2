from flask import Flask

app = Flask(__name__)

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
