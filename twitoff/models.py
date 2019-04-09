"""SQLAlchemy models for TwitOff."""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model): #subclass of Model class
    """Twitter users that we pull and analyze tweets for."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.name)

class Tweet(DB.Model):
    """Tweets."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(280))  #unicode supports emojis and other special charac.
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))
    # ORM is going to give us a way to get tweets from users and vice-versa.
    # Tweets field will have all the tweets from that user and it will not be stored in the DB.
    # It will be generated lazily at execution time, so that for a user we can pull all the tweets conveniently,
    #  without having to write an additional query.

    def __repr__(self):
        return '<Tweet {}>'.format(self.text)