#!/usr/bin/env python3
"""a module on babel
"""
from flask import request

@babel.localeselector
def get_locale():
    """determine the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])
