#!/usr/bin/env python3
""" Mock logging in """
from flask import Flask, render_template, g, request
from flask_babel import Babel, _
from typing import Dict, Union
import pytz
import datetime


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
    """ 1. Check if locale parameter is present in the request URL """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # 2. Locale from user settings
    if (
        hasattr(g, 'user') and g.user and 'locale' in g.user and
        g.user['locale'] in app.config['LANGUAGES']
    ):
        return g.user['locale']

    # 3. Locale from request headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])

    # 4. Default locale (fallback if none of the above conditions are met)
    return app.config['BABEL_DEFAULT_LOCALE']


# Define get_user function to get user details based on user ID
def get_user(user_id: int) -> Union[Dict[str, Union[str, None]], None]:
    """ Get user details based on user ID """
    return users.get(int(user_id))


# Define before_request function to execute before all other functions
@app.before_request
def before_request():
    """ Check if login_as parameter is present in the request URL """
    user_id = request.args.get('login_as')
    if user_id:
        user = get_user((user_id))
        g.user = user if user else None
    else:
        g.user = None


@babel.timezoneselector
def get_timezone():
    """Infer appropriate time zone."""
    url_timezone = request.args.get('timezone')
    if url_timezone and is_valid_timezone(url_timezone):
        return url_timezone

    # Find time zone from user settings
    if hasattr(g, 'user') and g.user and 'timezone' in g.user and is_valid_timezone(g.user['timezone']):
        return g.user['timezone']

    # Default to UTC
    return 'UTC'

def is_valid_timezone(timezone):
    """ Check if the provided timezone is valid """
    try:
        pytz.timezone(timezone)
        return True
    except pytz.exceptions.UnknownTimeZoneError:
        return False


@app.route('/')
def index() -> str:
    """ rendering index html """
    current_time = datetime.datetime.now(pytz.timezone(get_timezone()))

    formatted_current_time = current_time.strftime("%b %d, %Y, %I:%M:%S %p")

    return render_template('index.html', current_time=formatted_current_time)


if __name__ == '__main__':
    app.run(debug=True)
