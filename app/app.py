from flask import Flask, g
from flask.ext.sqlalchemy import SQLAlchemy
from config import Configuration
from flask.ext.login import LoginManger, current_user

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

login_manager = LoginManger(app)
login_manager.login_view = "login"

@app.before_request
def _before_request():
	g.user = current_user