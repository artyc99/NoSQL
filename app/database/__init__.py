from pymongo import MongoClient

__CONNECTION_STRING = 'mongodb://localhost:27117'

mongo_db_connection: MongoClient = MongoClient(__CONNECTION_STRING)
