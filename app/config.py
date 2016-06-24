import os

class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "oracle+cx_oracle://NEW_APP_OWNER:NEW_APP_OWNER@192.168.1.35:1521/SYS15DB"
    SECRET_KEY = "stuff"
