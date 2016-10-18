#import pymongo
from pymongo import MongoClient


links=[]
category=[]
client=MongoClient()
db=client.mydb
content=db.content

for i in content.find():
    print (i)