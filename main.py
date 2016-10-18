#import pymongo
from pymongo import MongoClient
from crawler import crawl

links=[]
category=[]
client=MongoClient()
db=client.mydb
content=db.links

for i in content.find():
        url=str(i['link'])
        categ=str(i['category'])
        links.append(url)
        category.append(categ)

crawl(links,category)