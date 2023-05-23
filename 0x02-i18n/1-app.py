#!/usr/bin/env python3
"""a module on babel"""
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)
app.config.from_object(Config)


class Config:
    """Config class that has a LANGUAGES class attribute
       equal to ["en", "fr"]
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
