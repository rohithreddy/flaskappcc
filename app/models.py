import datetime, re
from app import db

def slugify(s):
    return re.sub('[^\w]+', '-', s).lower()


class Person(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    dob = db.Column(db.String(255))
    slug= db.Column(db.String(64))
    email = db.Column(db.String(255), unique=True)
    phone_no = db.Column(db.String(255))
    password = db.Column(db.String(255))
    registered_at = db.Column(db.DateTime)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.generate_slug()


    def generate_slug(self):
        if self.first_name:
            self.slug = slugify(self.first_name)


class Recharge(db.Model):
    """docstring for ClassName"""
    __tablename__ = 'recharges'
    id = db.Column(db.Integer, primary_key=True)
    phone_no = db.Column(db.String(255))
    rec_type = db.Column(db.String(255))
    amount = db.Column(db.Integer)

    def __init__(self,phone_no, rec_type, amount):
        self.phone_no = phone_no
        self.rec_type = rec_type
        self.amount = amount

