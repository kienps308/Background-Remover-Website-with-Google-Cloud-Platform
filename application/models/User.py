from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column
from flask_login import UserMixin

base = declarative_base()
class User(UserMixin, base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = Column(String(), unique=True)
    password = Column(String())
    Usname = Column(String())