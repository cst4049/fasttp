from pymongo import MongoClient


class MongoClientA:
    def __init__(self):
        self.client = None
        self.db = None

    def init_config(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client.get_database()

    @staticmethod
    def execute(func, *args, **kwargs):
        return func(*args, **kwargs)


mongo_client = MongoClientA()
