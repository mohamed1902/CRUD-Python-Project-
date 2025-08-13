#DataBase
from pymongo import MongoClient

class mongoDB:
    def __init__(self , url="mongodb://localhost:27017" , db_name = "testdb"):
        self.clint= MongoClient(url)
        self.db= self.clint[db_name]

    def get_collection(self , collection_name):
        return self.db[collection_name]
    
mongo = mongoDB()