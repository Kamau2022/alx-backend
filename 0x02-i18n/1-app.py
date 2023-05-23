#!/usr/bin/env python3
"""babel"""
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]


class Config(app=None, default_locale='en', default_timezone='UTC')
