#!/usr/bin/env python3
""" Get locale from request """
from flask import Flask, render_template, request
from flask_babel import Babel, _


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
def get_locale():
    """ get_locale function """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ rendering index html """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
