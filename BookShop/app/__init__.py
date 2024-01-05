from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
import cloudinary
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = '^%^&$^T&*Y(*&*^&*^*(&&*$^4765876986764^&%&*%^%$&*^(*^*%*&^436'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:%s@localhost/bookdb?charset=utf8mb4' % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_RECORD_QUERIES"] = True
app.config["PAGE_SIZE"] = 6

db = SQLAlchemy(app=app)

cloudinary.config(
    cloud_name='diwrqtpmf',
    api_key='683474824977534',
    api_secret='A_7IwCcd0EOiMXkFjn33MlF39rU'
)

login = LoginManager(app = app)