from flask import Flask
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from flask_sqlalchemy import SQLAlchemy
# Create an instance of the Flask class
app = Flask(__name__)

# Add database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

app.config['SECRET_KEY'] = 'your_secret_key_here'
db = SQLAlchemy(app)

from application.models import User

from application import routes
