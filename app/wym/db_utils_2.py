from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database
import psycopg2
Base = declarative_base()

class User(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    mail = Column(String)
    comment = Column(String)
    phone = Column(String)


def get_engine():
    return create_engine('postgresql+psycopg2://test:testpassword@172.17.0.2/website', echo=True)

def verify_database():
    engine = get_engine()
    if not database_exists(engine.url):
        print('Creating Database')
        create_database(engine.url)
    else:
        print('Database already exists')

def get_session(engine):
    Session = sessionmaker()
    Session.configure(bing=engine)
    return Session()

if __name__ == '__main__':
    verify_database()
    engine = get_engine()
    

    Base.metadata.create_all(engine)


    # create table contact

    # test binding user 

    test_user = User(name='raph', mail='ra@bou.fr', comment='Great!')

    session.add(test_user)

    session.commit()
