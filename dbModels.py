from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mysqldb import MySQL
import pymysql as mysql


class used_cars(db.Model):
    __tablename__= "used_cars"
    car_id = db.Column(db.String(50), primary_key = True)
    make_id = db.Column(db.String(50), db.ForeignKey('car_make.make_id'))
    price = db.Column(db.Integer)
    milage = db.Column(db.Integer)
    category_id = db.Column(db.String(50), db.ForeignKey('category.category_id'))
    year = db.Column(db.Integer)
    image_link = db.Column(db.String(245))
    seller_id = db.Column(db.String(35), db.ForeignKey('seller.seller_id'))
    ulez = db.Column(db.String(20))
    owners = db.Column(db.Integer)


class car_make(db.Model):

    make_id = db.Column(db.String(20), primary_key = True)
    make = db.Column(db.String(25))
    model = db.Column(db.String(50))
    car_make = db.relationship('used_cars', backref='car_make', lazy=True)


class car_specifications(db.Model):

    spec_id = db.Column(db.String(20), primary_key = True)
    bhp  = db.Column(db.String(20))
    engine = db.Column(db.String(10))
    transmission = db.Column(db.String(20))
    fuel = db.Column(db.String(20))

class category(db.Model):

    category_id = db.Column(db.String(25), primary_key = True)
    category_type = db.Column(db.String(25))
    cat_used_cars = db.relationship('used_cars', backref='category', lazy=True)

class location(db.Model):

    location_id = db.Column(db.String(25), primary_key = True)
    town = db.Column(db.String(50))
    country = db.Column(db.String(25))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    seller = db.relationship('seller', backref='location', lazy=True)

class seller(db.Model):

    seller_id = db.Column(db.String(25), primary_key = True)
    location_id = db.Column(db.String(25), db.ForeignKey('location.location_id'))
    seller_name = db.Column(db.String(10))

class used_cars_specs(db.Model):

    car_id = db.Column(db.String(30), db.ForeignKey('used_cars.car_id'), primary_key = True)
    spec_id = db.Column(db.String(25),db.ForeignKey('car_specifications.spec_id'), primary_key = True)

class users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(255))

    def __init__(self, id, password, email, fullname):
        self.id = id
        self.password = password
        self.fullname= fullname
        self.email=email

