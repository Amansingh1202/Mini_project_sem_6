from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./database/database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column("movie_id", db.Integer, primary_key=True)
    movie_name = db.Column(db.String(30))
    average_score = db.Column(db.Float)
    children = relationship("Child")


class Comments(db.Model):
    id = db.Column("comments_id", db.Integer, primary_key=True)
    comment = db.Column(db.String(120))
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"))


db.create_all()