from app.main import db
import datetime

class Post(db.Model):
    """
    Defines the table schema for raw posts being delivered to database
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.String(10), unique=True, nullable=False)
    subreddit = db.Column(db.String(30), nullable=False)
    shortlink = db.Column(db.String(30), nullable=False)
    created_utc = db.Column(db.DateTime, nullable=False)
    created_local = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(300), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    body = db.Column(db.Text, nullable=False)
    num_comments = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    up_ratio = db.Column(db.Float(10), unique=True)
    nsfw = db.Column(db.Boolean, nullable=False)
    is_edited = db.Column(db.Boolean, unique=True)
    flair = db.Column(db.String(20), unique=True)
    spoiler = db.Column(db.Boolean, nullable=True)
    awards = db.Column(db.Integer, nullable=True)