import mysql.connector
import sqlalchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:abc123@localhost:3306/dbtestowa',echo=True)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=True))
    fullname = sqlalchemy.Column(sqlalchemy.String(length=True))
    nickname = sqlalchemy.Column(sqlalchemy.String(length=True))

    def __repr__(self):
        return f"<User --> name:{self.name}, fullname = {self.fullname}, nickname = {self.nickname}.>"
      
