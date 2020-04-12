from pymongo import MongoClient
client = MongoClient('localhost',27017)

db = client.PYDB
db.UserProfile.update_one({'name':'dugu'},{'$set':{'age':'4'}})
userData = db.UserProfile.find({})

for x in userData:
    print('{0} {1} {2}'.format(x['name'], x['address'], x['age']))
#1

# print(db.UserProfile.)
