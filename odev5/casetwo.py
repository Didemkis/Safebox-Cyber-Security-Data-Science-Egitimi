from pymongo import MongoClient

client = MongoClient("mongodb+srv://didem:didem@flaskmongodb.qkroipj.mongodb.net/")
db = client.get_database('flaskmongodb')



for document in db['Users'].find():#tum kullanicilari getirir
    print(document)
print("\n")


for document in db['Users'].find({"Name": "Ahmet"}):#Name adi Ahmet olanlari getirir
    print(document)
print("\n")


for document in db['Users'].find({"Age": {"$gt": 20}}):#Age'i 20'den buyuk olanlari getirir
    print(document)
print("\n")


update_query = {"Age": {"$gt": 25}}
new_values = {"$set": {"Job Description": 0}}
x = db['Users'].update_many(update_query, new_values)#Age'i 25'ten buyuk olanlarin Job Description'ini 0 yapar
print(x.modified_count, "documents updated.")


remove_query = {"Age":{"$gte":40,"$lt":48}}
x = db['Users'].delete_many(remove_query)#Age'i 40 ile 48 arasinda olanlari siler
print(x.deleted_count, "documents deleted.")
