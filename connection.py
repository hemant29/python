import pymongo
import dns # required for connecting with SRV

client = pymongo.MongoClient("mongodb+srv://kay:myRealPassword@cluster0.mongodb.net/test?w=majority")
db = client.test