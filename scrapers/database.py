from pymongo import MongoClient

class Mongo_Database: #
    def __init__(self):
        self.client=MongoClient()
        self.db=self.client.test

    def store_single(self, data):
        result=self.db.bitsentiment.insert_one(data)   
