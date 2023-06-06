from pymongo import MongoClient
import random

NAMES = ['Ali', 'Ahmet', 'Ayse', 'Selim', 'Fatih']
JOBS = ['engineer', 'teacher', 'farmer', 'singer', 'driver']
AGE = random.randrange(0, 50)
JOB_DESCRIPTION = 1

client = MongoClient("mongodb+srv://didem:didem@flaskmongodb.qkroipj.mongodb.net/")
db = client.get_database('flaskmongodb')

random_user = {"Name": random.choice(NAMES),
               "Age": AGE,
               "Job": random.choice(JOBS),
               "Job Description": JOB_DESCRIPTION}

db['Users'].insert_one(random_user)
