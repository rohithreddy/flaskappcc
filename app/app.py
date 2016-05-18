from flask import Flask, g
from flask.ext.sqlalchemy import SQLAlchemy
from config import Configuration
from flask.ext.login import LoginManager, current_user
from flask.ext.bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"

@app.before_request
def _before_request():
	g.user = current_user

bcrypt = Bcrypt(app)