from pymongo import MongoClient

client = MongoClient()
db = client.mydb
content = db.user_data


def response_type(user, article_id, category, response):
    post = {"user": user,
            "article_id": article_id,
            "category": category,
            "response": response
            }
    content.insert_one(post)
