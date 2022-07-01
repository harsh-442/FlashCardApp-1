from flask import Flask, request, redirect, url_for, render_template, flash
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


@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        try:
            uname=request.form["username"]
            pswd=request.form["password"]
            return redirect(url_for("dashboard"))
        except:
            flash("Login error!\nTry Again")
            pass
            
        

@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method=="GET":
        return render_template("signup.html")
    else:
        uname=request.form["username"]
        p1=request.form["password1"]
        p2=request.form["password2"]
        if p1!=p2:
            flash("Passwords do not match!")
        else:
            user=User(user_name=uname,password=p1)
            db.session.add(user)
            db.session.commit()

@app.route("/", methods = ["GET","POST"])
def dashboard():
    deckno=0
    return render_template("dash.html",deckno=deckno)

@app.route("/profile",methods=["GET"])
def profile():
    return render_template("profile.html")

@app.route("/adddecks")
def adddecks():
    if request.method == "GET":
        return render_template("adddecks.html")
    else:
        dname = request.form["name"]
        d_desc = request.form["description"]

if __name__=="__main__":
    app.run(debug=True)