#import pymongo
from pymongo import MongoClient
import json


links = []
category = []
client = MongoClient()
db = client.mydb
content = db.meta_data
a=None
b=None
c=None
n=[]
post = {"category": "Y",
        "extra": "W"}
for i in content.find():
    #print i
    n.append(i)

print str(n)
#print x
#if x.count() == 0:
#    print "yes"
#    content.insert_one(post)
#else:
#    print "no"
    #content.insert_one(post)


