from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = "postgres+psycopg2://virginie:mysecretpassword@db:5432/app_v_r_d"
engine = create_engine(DATABASE_URI)
base = declarative_base()

class Contact(base):
    __tablename__ = "contact"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    message = Column()

Session = sessionmaker(engine)
session = Session()

base.metadata.create_all(engine)

def insert_db(session, list_params):
    new_contact = Contact(name = list_params[0], email=list_params[1], phone=list_params[2], message= list_params[3])
    session.add(new_contact)
    session.commit()

def fetch_db(session):
    contact = session.query(Contact)
    return contact

info_contact = ["virgi", "virgi@yopmail.com", "0123456787", "coucou"]
insert_db(session, info_contact)