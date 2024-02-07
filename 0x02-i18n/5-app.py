#!/usr/bin/env python3
""" Mock logging in by creating a user login system """
from flask import Flask, render_template, g, request
from flask_babel import Babel, _
from typing import Dict, Union


app = Flask(__name__)
babel = Babel(app)


# Define user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Supported languages list."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Use the Config class as the configuration for the Flask app
app.config.from_object(Config)


# Define supported locales using request.accept_languages
@babel.localeselector
def get_locale() -> str:
    """ Check if locale parameter is present in the request URL """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


# Define get_user function to get user details based on user ID
def get_user(user_id: int) -> Dict:
    """ Get user details based on user ID """
    return users.get(int(user_id))


# Define before_request function to execute before all other functions
@app.before_request
def before_request():
    """ Check if login_as parameter is present in the request URL """
    user_id = (request.args.get('login_as', 0))
    g.user = get_user(user_id)


@app.route('/')
def index() -> str:
    """ rendering index html """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
