from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class MysqlClient:
    def __init__(self):
        self.Base = declarative_base()
        self.SessionLocal = None
        self.engine = None

    def init_config(self, uri, **kwargs):
        engine = create_engine(uri, **kwargs)
        self.engine = engine
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def create_table(self):
        self.Base.metadata.create_all(bind=self.engine)

    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def get_db_sync(self):
        db = self.SessionLocal()
        return db


mysql_client = MysqlClient()
