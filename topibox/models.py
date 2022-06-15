from topibox import db
import sqlalchemy as sa

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

class Audiobook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(256), unique=True, nullable=False)
    title = db.Column(db.String(256))
    author = db.Column(db.String(200))
    playcount = db.Column(db.Integer, default=0)
    added_on = db.Column(db.DateTime)
