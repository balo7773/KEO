from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('mysql+mysqlconnector://blog73:blog147773@172.22.54.54/blogdb')

Base = declarative_base()

#class users with table user
class users(Base):
    __tablename__ = 'user'
    
    signup_id = Column(Integer, ForeignKey('registration.id'))
    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(25))
    passwd = Column(String(50), unique=True)
    
    signup = relationship("Signup", back_populates="user")

    def repr(Signup):
        return f"user is {users.uname} , email is {users.email}"

#class signup with registration table
class Signup(Base):
    __tablename__ = 'registration'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(25), nullable=False)
    passwd = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    
    user = relationship("users", back_populates="signup", uselist=False)
    
    def repr(Signup):
        return f"user is {Signup.uname} , email is {Signup.email}"

Base.metadata.create_all(engine)  # Creates all tables


Session = sessionmaker(bind=engine)
session = Session()
