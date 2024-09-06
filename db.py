from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('mysql+mysqlconnector://blog73:blog147773@172.22.54.54/blogdb')

Base = declarative_base()

#class signup with registration table
class Signup(Base):
    __tablename__ = 'registration'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    uname = Column(String, nullable=False)
    passwd = Column(String, unique=True, nullable=False)
    
    user = relationship("User", back_populates="signup", uselist=False)

#class users with table user
class users(Base):
    __tablename__ = 'user'
    
    signup_id = Column(Integer, ForeignKey('registration.id'))
    uname = Column(String)
    passwd = Column(String, unique=True)
    
    signup = relationship("Signup", back_populates="user")



Session = sessionmaker(bind=engine)
session = Session()
