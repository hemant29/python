import pymongo
connection = pymongo.MongoClient('mongodb://hemant55:hk291199@cluster0-rimsj.mongodb.net')
database = connection ['mydb_01']
collection = database['mycol_01']
data = {'name':"hemant"}
collection.insert_one(data) 