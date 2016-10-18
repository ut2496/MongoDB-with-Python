from pymongo import MongoClient
from similarity import get_similarity

client = MongoClient()
db = client.mydb
content = db.content
similar_to=[]
temp = 0

def similarity_matcher(final_article,url):
    flag=0
    if content.count()==0:
        print("hello")
    else:
        for i in content.find():
            db_url=str(i['url'])
            article=str(i['article'])
            post_id=str(i["_id"])

            if db_url != url:
                sim_value=get_similarity(final_article,article)
                print (sim_value)
                if sim_value>=.3:
                    similar_to.append(post_id)
                    flag=1
            else:
                return 1



def insertion(category,url,final_article4):
    temp_2 = similarity_matcher(final_article4,url)

    if(temp_2==1):
        print ("Article already exists in database")
    else:
        post = {"category": category,
                "url": url,
                "article": final_article4,
                "similar to": similar_to}

        content.insert_one(post)

