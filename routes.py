from app import app
from db import db
from flask import render_template, request, redirect
from sqlalchemy.sql import text
import users, listings

@app.route("/")
def index():
    #list = messages.get_list()
    result = db.session.execute(text("SELECT id, title, pickup_date, pickup_location, dropoff_location FROM listings ORDER BY pickup_date ASC"))
    listings = result.fetchall()
    return render_template("index.html", listings=listings)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")
        
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
        
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/listing", methods=["GET", "POST"])
def listing():
    if request.method == "GET":
        return render_template("listingnew.html")
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        pickup_location = request.form["pickup_location"]
        dropoff_location = request.form["dropoff_location"]
        date = request.form["date"]

        if listings.new(title, description, pickup_location, dropoff_location, date):
            return redirect("/")
        else:
            return render_template("error.html", message="Ilmoituksen lisääminen ei onnistunut")
        

@app.route('/listing/<int:listing_id>')
def listing_details(listing_id):
    sql = text("SELECT * FROM listings WHERE id=:id")
    result = db.session.execute(sql, {"id":listing_id})
    listing = result.fetchone()
    if listing:
        return render_template('listing.html', listing=listing)
    else:
        return render_template("error.html", message="404")