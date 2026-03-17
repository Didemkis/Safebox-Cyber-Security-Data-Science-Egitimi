from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://didem:didem@flaskmongodb.qkroipj.mongodb.net/")
db = client.get_database('flaskmongodb')

from flask import Flask

app = Flask(__name__)

user = {"Name": "Metin",
        "Age": 26,
        "Job": "farmer",
        "Job Description": 1}

@app.route('/adduser', methods=['POST'])
def adduser():
   db['Users'].insert_one(user)
   return "User added successfully!"

@app.route('/25', methods=['GET'])
def fetch_greater_than():
    db_list = []
    query_string={"Age": {"$gt": 25}}
    for document in db['Users'].find(query_string):
        db_list.append(document)
    return str(db_list)

@app.route('/', methods=['GET'])
def fetch_all():
    db_list = []
    for document in db['Users'].find():
        db_list.append(document)
    return str(db_list)

@app.route('/deleteuser', methods=['GET', 'POST'])
def delete_by_id():
    _id = '647e1b6dbcb18068735a1d17'
    db['Users'].delete_one({'_id': ObjectId(_id)})
    return "User by given id has been deleted!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
