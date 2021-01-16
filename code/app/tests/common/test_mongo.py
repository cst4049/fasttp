from app.common.db_mongo import mongo_client
from settings import mongo_settings


def test_mongo():
    mongo_client.init_config(mongo_settings.uri)
    item = mongo_client.execute(mongo_client.db['test'].find_one, {'a': 'b'})
    print(item)


test_mongo()
