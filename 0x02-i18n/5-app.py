#!/usr/bin/env python3
"""a module to get locale from request
"""
from flask_babel import Babel
from flask import Flask, render_template, request, g

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config class that has a LANGUAGES class attribute
       equal to ["en", "fr"]
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """function that returns a user dictionary or None if the
       ID cannot be found or if login_as was not passed.
    """
    try:
        user_id = request.args.get('login_as', None)
        return users.get(int(user_id), None) if user_id is not None else None
    except Exception:
        return None


@app.before_request
def before_request() -> None:
    """uses get_user to find a user if any,
       and set it as a global on flask.g.user.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """determine the best match with our supported languages
    """
    for parameter in request.query_string.decode('utf-8').split('&'):
        try:
            key, value = parameter.split('=')
            if key == 'locale' and value in app.config["LANGUAGES"]:
                return value
        except ValueError:
            continue
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def index():
    """a function that returns index page
    """
    try:
        return render_template("5-index.html")
    except ValueError as exception:
        print(exception.__str__())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
