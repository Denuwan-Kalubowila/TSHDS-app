import os
from threading import Lock
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

class MongoDB(object):
    def __init__(self) -> None:
        self._CONNECTION_STRING=os.getenv(key='MONGO_URI')
        self._client=None
        self.lock=Lock()
        
    def connectDB(self, databaseName:str, collectionName:str):
        if self._client is None:
            with self.lock:
                if self._client is None:
                    client=MongoClient(self._CONNECTION_STRING)
                    database=client[collectionName]
                    collection=database[databaseName]
                    
        return  client, database, collection

