import datetime, re
from app import db


class Person(db.Model):
	__tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(255))
    lname = db.Column(db.String(255))
    dob = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True)
    phone_no = db.Column(db.String(255))
    password = db.Column(db.String(255))
    registered_at = db.Column(db.DateTime)

class Recharge(db.Model):
	"""docstring for ClassName"""
	__tablename__ = 'recharges'
	id = db.Column(db.Integer, primary_key= True)
	phone_no = db.Column(db.String(255))
	rec_type = db.Column(db.String(255))
	amount = db.Column(db.Integer)



