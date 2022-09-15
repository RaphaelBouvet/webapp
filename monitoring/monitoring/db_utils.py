import datetime

from sqlalchemy import (
    create_engine,
    Column, Integer, String, Float, DateTime
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy.sql import func


class PGSQL_DB(object):
    def __init__(self, user='virginie', password='mysecretpassword', host='db', port=5432):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        # default database:
        self.db = 'app_v_r_d'
        self.base_url = f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/"

        self.engine = None

    def connect_to_default_db(self):
        url = self.base_url + self.db
        self.engine = create_engine(url, client_encoding='utf8', echo=True)
        print(database_exists(self.engine.url))
        return self.engine

    def connect_to_db(self, db_name):
        url = self.base_url + db_name
        self.engine = create_engine(url, client_encoding='utf8', echo=True)

        if not database_exists(self.engine.url):
            create_database(self.engine.url)

        if database_exists(self.engine.url):
            return self.engine
        else:
            raise Exception(f"Could not connect to {db_name!r} (database doesn't exist)")

    def delete_db(self, db_name):
        url = self.base_url + db_name

        self.engine = create_engine(url, client_encoding='utf8', echo=True)
        if database_exists(self.engine.url):
            drop_database(self.engine.url)

        print(database_exists(self.engine.url))

    def get_table(self, table_name=None):
        session = sessionmaker(bind=self.engine)
        with session.begin() as session:
            query = session.query(Text_Summ).all()
            session.expunge_all()
        return query

Base = declarative_base()
class Text_Summ(Base):
    __tablename__ = 'text_summarize'

    id = Column(Integer, primary_key=True, autoincrement=True)
    input_text = Column(String)
    output_text = Column(String)
    date_request = Column(DateTime, server_default=func.now())
    time_treated = Column(Float)

