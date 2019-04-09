"""Entry point fro TwitOff Flask application."""

from .app import create_app

APP = create_app #capitalized since its a global variable.