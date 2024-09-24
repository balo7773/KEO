#!/usr/bin/python3
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from flask_login import UserMixin
from .config import Config

engine = create_engine(Config.SQL_ALCHEMY_URI)

Base = declarative_base()

#class users with table user
class users(Base, UserMixin):
    __tablename__ = 'user'
    
    signup_id = Column(Integer, ForeignKey('registration.id'))
    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(25))
    passwd = Column(String(50), unique=True)
    
    signup = relationship("Signup", back_populates="user")

    def __repr__(self):
        return f"user is {self.uname}, email is {self.signup.email}"

    
#class signup with registration table
class Signup(Base, UserMixin):
    __tablename__ = 'registration'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(25), nullable=False)
    passwd = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    
    user = relationship("users", back_populates="signup", uselist=False)
    
    def repr(self):
        return f"user is {self.uname} , email is {self.email}"

    def get_id(self):
        return str(self.id)  # Flask-Login expects this to return a string

Base.metadata.create_all(engine)  # Creates all tables


Session = sessionmaker(bind=engine)
session = Session()
