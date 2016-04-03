from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Db:
    def __init__(self, app):
        self.engine = create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'))
        self.Base = declarative_base()
        self.SessionMaker = sessionmaker(bind=self.engine)
        self.session = self.SessionMaker()