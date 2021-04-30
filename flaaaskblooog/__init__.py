from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '35164fcf0f4a8727457816929189b17e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/flask_blog04/site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager1001=LoginManager(app)
login_manager1001.login_view='login'
login_manager1001.login_message_category='info'

from flaaaskblooog import routes