#!/usr/bin/env python3
"""flask application
"""
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    """a function that returns index page
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
