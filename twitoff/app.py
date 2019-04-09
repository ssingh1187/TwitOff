"""Main application and logic for TwitOff."""

from flask import Flask
from .models import DB

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3' #app knows about database here
    DB.init_app(app) #database knows about app here

    @app.route('/')
    def root():
        return 'Welcome to TwitOff!'

    return app