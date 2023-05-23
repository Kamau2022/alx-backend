#!/usr/bin/env python3
"""a module on babel
"""
from flask import request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)

@babel.localeselector

def get_locale():
    """determine the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])
