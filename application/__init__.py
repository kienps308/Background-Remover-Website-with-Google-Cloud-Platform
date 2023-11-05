from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

from application import routes
