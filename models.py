from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__="user"
    user_id = db.Column(db.Integer,autoincrement=True,primary_key="True")
    user_name = db.Column(db.String,unique=True,nullable=False)
    password = db.Column(db.String,nullable=False)
    decks = db.relationship("Decks")
    
class Decks(db.Model):
    __tablename__="decks"
    deck_id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    deck_name = db.Column(db.String,unique=True,nullable=False)
    deck_description = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'),nullable=False)
    cards = db.relationship("Cards")
    
class Cards(db.Model):
    __tablename__ = "cards"    
    card_id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    card_front = db.Column(db.String,nullable=False)
    card_back = db.Column(db.String,nullable=False)
    deck_id = db.Column(db.Integer,db.ForeignKey('decks.deck_id'),nullable=False)