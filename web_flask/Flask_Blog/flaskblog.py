#!/usr/bin/python3

from flask import Flask, request
from markupsafe import escape
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
