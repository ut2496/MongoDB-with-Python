import os
from pymongo import MongoClient
from file_count import file_count
client = MongoClient()
db = client.mydb
content = db.content
similar_to = []


def insertion(category, url, final_article4, str_article_title, image_url):
    temp_2 = duplicate_checker(url)
    if temp_2 == 1:
        print ("Article already exists in database")
    else:
        path, art_id = text_file_creation(category, final_article4)
        post = {"category": category,
                "url": url,
                "article_id": art_id,
                "title": str_article_title,
                "image_url": image_url,
                "path": path}
        content.insert_one(post)


def duplicate_checker(url):
    flag = 0
    if content.count() == 0:
        flag = 0
    else:
        checker = content.find({"url": url})
        for i in checker:
            flag = 1
    return flag


def text_file_creation(category, final_article):
    name = file_count(category)
    temp = str(name)
    if os.path.exists('C:/zeus/' + category + '/' + temp + '.txt'):
        print "File exists"
        name += 1

    temp = str(name)
    f = open('C:/zeus/' + category + '/' + temp + '.txt', 'w')
    path_temp = 'C:/zeus/' + category + '/' + temp + '.txt'
    f.write(final_article)
    f.close()
    return path_temp, temp
