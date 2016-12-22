from pymongo import MongoClient

client = MongoClient()
db = client.mydb
content = db.content


def path_finder(category, article_id):
    for i in content.find({"category": category, "article_id": article_id}):
        return i['path']