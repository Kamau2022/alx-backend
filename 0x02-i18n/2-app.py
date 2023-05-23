#!/usr/bin/env python3
"""a module on babel
"""
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    """a function that returns index page
    """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])
