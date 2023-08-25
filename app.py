"""Blogly application."""

from flask import Flask
from models import db, connect_db
from flask_debugtoolbar import DebugToolbarExtension

app.config['SECRET_KEY'] = "tis-a-secret"
debug = DebugToolbarExtension(app)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()
