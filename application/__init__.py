from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from google.cloud.sql.connector import Connector, IPTypes
import secrets

secret = secrets.token_urlsafe(32)

# init SQLAlchemy so we can use it later in our models
# initialize Python Connector object
connector = Connector()

# initialize parameters
project_id='utopian-splicer-400911'
region = 'europe-west2'
instance_name = 'kienps'

INSTANCE_CONNECTION_NAME = f"{project_id}:{region}:{instance_name}" # i.e demo-project:us-central1:demo-instance
print(f"Your instance connection name is: {INSTANCE_CONNECTION_NAME}")
DB_USER = "user"
DB_PASS = "test"
DB_NAME = "cloud_project_4"

# Python Connector database connection function
# function to return the database connection object
def getconn():
    conn = connector.connect(
        INSTANCE_CONNECTION_NAME,
        "pymysql",
        user=DB_USER,
        password=DB_PASS,
        db=DB_NAME
    )
    return conn

app = Flask(__name__)

# initialize the app with the extension
db = SQLAlchemy()

def create_app():
    # configure Flask-SQLAlchemy to use Python Connector
    app.secret_key = secret
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        "creator": getconn
    }

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models.User import User
    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .views import views as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
