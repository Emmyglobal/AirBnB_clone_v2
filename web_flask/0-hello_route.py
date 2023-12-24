#!/usr/bin/python3
"""
A script that starts a web Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display "Hello HBNB!"
You must use the option strict_slashes=False in your route definition
"""

from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)


def hello():
    """Returns a string"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


