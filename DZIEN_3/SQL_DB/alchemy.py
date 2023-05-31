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
    name = sqlalchemy.Column(sqlalchemy.String(length=50))
    fullname = sqlalchemy.Column(sqlalchemy.String(length=50))
    nickname = sqlalchemy.Column(sqlalchemy.String(length=50))

    def __repr__(self):
        return f"<User --> name:{self.name}, fullname = {self.fullname}, nickname = {self.nickname}.>"

Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

usr1 = User(name='Marcin', fullname='Marcin Albiniak' , nickname='albim')
session.add(usr1)
usr2 = User(name='Anna', fullname='Anna Koc' , nickname='kocyk')
session.add(usr2)
usr3 = User(name='Olaf', fullname='Olaf Byk' , nickname='byczek')
session.add(usr3)
usr4 = User(name='Roma', fullname='Roma Nowik' , nickname='romcia')
session.add(usr4)

session.commit()

print("_"*25)
for s in session.query(User).all():
    print(s.fullname)

print("_"*25)
for s in session.query(User).filter(User.nickname=="romcia"):
    print(s.fullname)

