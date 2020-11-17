from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Secret key
app.config['SECRET_KEY'] = 'e33cc6fcf38be4c8f4062ab1fae038b3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# create an SQLAlchemy Database instance
db = SQLAlchemy(app)

from flaskblog import routes