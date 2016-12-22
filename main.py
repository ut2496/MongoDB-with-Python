# import pymongo
from pymongo import MongoClient
from crawler import crawl
from similarity import similarity_list


links = []
category = []
client = MongoClient()
db = client.mydb
content = db.links

for i in content.find():
        url = str(i['link'])
        categ = str(i['category'])
        links.append(url)
        category.append(categ)

crawl(links, category)
for i in (0, len(category)):
        similarity_list(category[i])
