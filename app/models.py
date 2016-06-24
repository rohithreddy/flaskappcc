import datetime, re
from app import db, login_manager, bcrypt
from sqlalchemy import Table, Column, event, Integer, String
from sqlalchemy.schema import Sequence

def slugify(s):
    return re.sub('[^\w]+', '-', s).lower()

# @event.listens_for(Table, "column_reflect")
# def column_reflect(inspector, table, column_info):
#     # set column.key = "attr_<lower_case_name>"
#     column_info['key'] = "attr_%s" % column_info['name'].lower()

@login_manager.user_loader
def _user_loader(user_id):
    return Person.query.get(int(user_id))

SEQUENCE_ID_CUST = Sequence('CUSTOMER_ID_SEQ',  increment=1)
SEQUENCE_ID_TRANS = Sequence('TRANS_ID_SEQ',  increment=1)

class Person(db.Model):
    __tablename__ = Table('TELE_CUST_DETAILS', db.metadata, autoload=True, autoload_with=db.engine)
    id = Column('CUSTOMER_ID', Integer, SEQUENCE_ID_CUST, primary_key=True, default=SEQUENCE_ID_CUST.next_value())
    name = Column('NAME', String)
    age = Column('AGE', Integer)
    income = Column('INCOME', Integer)
    gender = Column('GENDER', String)
    martial_status = Column('MARITAL_STATUS', String)
    address = Column('ADDRESS', String)
    email = Column('EMAIL_ID', String)
    phone_no = Column('MOBILE_NO', String)
    twitter_id = Column('TWITTER_ID', String)
    facebook_id = Column('FACEBOOK_ID', String)
    centre = Column('CENTRE', String)
    first_name = Column('FIRST_NAME', String)
    last_name = Column('LAST_NAME', String)
    family_name = Column('FAMILY_NAME', String)
    pincode = Column('PINCODE', Integer)
    city = Column('CITY', String)
    state = Column('STATE', String)
    country = Column('COUNTRY', String)
    dedupflag = Column('DEDUPE_FLAG_COLUMN', String)
    parent_key = Column('PARENT_KEY', Integer)
    batch_id = Column('BATCH_ID', Integer)
    record_id = Column('RECORD_ID', Integer)
    merge_id = Column('MERGE_ID', Integer)
    password_hash = Column('PASSWORD_HASH', String)
    active = Column('ACTIVE', Integer)

    def __init__(self, email, age, first_name, last_name, password_hash, *args, **kwargs):
        self.email = email
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.password_hash = password_hash
        super(Person, self).__init__(*args, **kwargs)


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
        return self.password_hash == raw_password

    # @classmethod
    # def create(cls, email, password, **kwargs):
    #     return Person(
    #         email = email,
    #         password_hash = Person.make_password(password),
    #         **kwargs
    #     )

    @staticmethod
    def authenticate(email, password):
        person = Person.query.filter(Person.email == email).first()
        if person and person.check_password(password):
            return person
        return False




class Recharge(db.Model):
    """docstring for ClassName"""
    __tablename__ = Table('TELE_CUST_TRANSACTIONS', db.metadata, autoload=True, autoload_with=db.engine)
    id = Column('TRANSACTION_ID', Integer,SEQUENCE_ID_TRANS , primary_key=True,  default=SEQUENCE_ID_TRANS.next_value())
    trn_cust_id = Column('TRN_CUST_ID', Integer)
    recharge_type = Column('PRODUCT', String)
    amount = Column('TRANSACTION_AMT', Integer)
    points = Column('POINTS', Integer)
    points_type = Column('POINTS_TYPE', SEQUENCE_ID_TRANS)
    phone_no = Column('MOBILE_NO', String)
    recharge_date = Column('RECHARGE_DATE', String)
    name = Column('NAME', String)
    email_id = Column('EMAIL_ID', String)
    cust_id = Column('CUST_ID', String)
    trans_is = Column('TRANS_ID', String)
    dedupe_flag_column = Column('DEDUPE_FLAG_COLUMN', String)
    parent_key = Column('PARENT_KEY', Integer)
    batch_id = Column('BATCH_ID', Integer)
    record_id = Column('RECORD_ID', Integer)
    merge_id = Column('MERGE_ID', Integer)





    def __init__(self, *args, **kwargs):
        super(Recharge, self).__init__(*args, **kwargs)
