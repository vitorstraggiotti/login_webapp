import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///userdata.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin","password")
session.add(user)

user = User("vitor","123456789")
session.add(user)

# commit the record the database
session.commit()
