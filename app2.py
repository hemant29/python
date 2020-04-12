#!flask/bin/python
from flask import Flask
from flask import request
from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client.PYDB

app = Flask(__name__)

app = Flask(__name__)
@app.route('/postjson', methods=['POST'])
def post():
    print(request.is_json)
    content = request.get_json()
    #print(content)
    print(content['id'])
    print(content['name'])
    return 'Hello ' + content['name']

@app.route('/users', methods=['GET'])
def getUser():
    pareter = request.args.get('name')
    userData = db.UserProfile.find_one({'name':pareter})
    data = userData['age']
    #for x in userData:
     #   print('{0} {1} {2}'.format(x['name'], x['address'], x['age']))
    data = '{0} {1} {2}'.format(userData['name'], userData['address'], userData['age'])
    
    return data

@app.route('/', methods=['GET'])
def root():
    
    return "Hi, Welcome to my Flask Python web service"

@app.route('/adduser', methods=['GET'])
def adduser():  
    print ('Starting')
    namedata = request.args.get('name')
    agedata = request.args.get('age')
    addressdata = request.args.get('address')

    print('{0} {1} {2}'.format(namedata,agedata,addressdata))
    db.UserProfile.insert({"name":namedata, "address":addressdata,"age":agedata})
    return "hi m here i am rechable"

@app.route('/adduserpost', methods=['POST'])
def adduserpost():
    print(request.is_json)
    content = request.get_json()
    db.UserProfile.insert({"name":content['name'],"address":content['address'],"age":content['age']})
    #print(content['id'])
    print(content['name'])
    return 'Hello ' + content['name']


app.run(host='127.0.0.1', port=5000)