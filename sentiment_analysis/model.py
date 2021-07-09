from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import app

db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column("movie_id", db.Integer, primary_key=True)
    movie_name = db.Column(db.String(30))
    average_score = db.Column(db.Float)


class Comments(db.Model):
    id = db.Column("comments_id", db.Integer, primary_key=True)
    comment = db.Column(db.String(120))
    review_status = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"))

