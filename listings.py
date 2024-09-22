from db import db
from sqlalchemy.sql import text
from datetime import datetime
import users

def new(title, description, pickup_location, dropoff_location, date):
    date = datetime.strptime(date, '%d.%m.%Y')
    user_id = users.user_id()
    print(users.user_id())
    sql = text("INSERT INTO listings (title,description,pickup_location,dropoff_location,pickup_date,owner_id) VALUES (:title,:description,:pickup_location,:dropoff_location,:pickup_date,:owner_id)")
    db.session.execute(sql, {"title":title, "description":description, "pickup_location":pickup_location, "dropoff_location":dropoff_location ,"pickup_date":date, "owner_id":user_id})
    db.session.commit()
    return True

