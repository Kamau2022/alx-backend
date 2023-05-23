#!/usr/bin/env python3
"""a module on babel
"""
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class that has a LANGUAGES class attribute
       equal to ["en", "fr"]
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """a function that returns index page
    """
    return render_template('2-index.html')
