import datetime, re
from app import db, login_manager, bcrypt

def slugify(s):
    return re.sub('[^\w]+', '-', s).lower()

@login_manager.user_loader
def _user_loader(user_id):
    return Person.query.get(int(user_id))

class Person(db.Model):
    ## __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    dob = db.Column(db.String(255))
    slug= db.Column(db.String(64))
    email = db.Column(db.String(255), unique=True)
    phone_no = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=True)
    registered_at = db.Column(db.DateTime)

    def __init__(self, *args, **kwargs):
        super(Person, self).__init__(*args, **kwargs)
        self.generate_slug()


    def generate_slug(self):
        if self.first_name:
            self.slug = slugify(self.first_name)

    # Flask-Login Interface
    def get_id(self):
        return str(self.id)


    def is_authenticated(self):
        return True


    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    @staticmethod
    def make_password(plaintext):
        return bcrypt.generate_password_hash(plaintext)

    def check_password(self, raw_password):
        return bcrypt.check_password_hash(self.password_hash, raw_password)

    @classmethod
    def create(cls, email, password, **kwargs):
        return Person(
            email = email,
            password_hash = Person.make_password(password),
            **kwargs
        )

    @staticmethod
    def authenticate(email, password):
        person = Person.query.filter(Person.email == email).first()
        if person and person.check_password(password):
            return person
        return False




class Recharge(db.Model):
    """docstring for ClassName"""
    #__tablename__ = 'recharges'
    id = db.Column(db.Integer, primary_key=True)
    phone_no = db.Column(db.String(255))
    email_id = db.Column(db.String(64))
    recharge_type = db.Column(db.String(255))
    amount = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):
        super(Recharge, self).__init__(*args, **kwargs)
