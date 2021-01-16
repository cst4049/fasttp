from app.common import mysql_client
from settings import mysql_settings
from app.models.heartbeat import Item


def test_mysql():
    mysql_client.init_config(mysql_settings.uri)
    mysql_client.create_table()
    db = mysql_client.get_db()
    data = db.query(Item).filter(Item.id == 1).first()
    print(data)
    db.close()
