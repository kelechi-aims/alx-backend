#!/usr/bin/env python3
""" Get locale from request """
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


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


@app.route('/')
def index() -> str:
    """ rendering index html """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
