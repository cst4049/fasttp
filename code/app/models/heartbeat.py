from sqlalchemy import Column, Integer, String
from app.common.db_mysql import mysql_client


class Item(mysql_client.Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(50))
