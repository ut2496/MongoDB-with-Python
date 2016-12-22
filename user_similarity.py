from pymongo import MongoClient
from path_finder import path_finder


def coefficient(u1_up, u1_down, u2_up, u2_down):
    up_count = 0
    down_count = 0
    u1_up_u2_down_count = 0
    u1_down_u2_up_count = 0

    total_list = list(set(u1_up + u1_down + u2_up + u2_down))

#    merged_upvote = list(set(u1_up + u2_up))
#    merged_downvote = list(set(u1_down + u2_down))

    for i in u1_up:
        if i in u2_up:
            up_count += 1
        if i in u2_down:
            u1_up_u2_down_count += 1

    for j in u1_down:
        if j in u2_down:
            down_count += 1
        if j in u2_up:
            u1_down_u2_up_count += 1

    total_value = len(total_list)
    positive_part = (float(up_count) + float(down_count))/float(total_value)
    negative_part = (float(u1_up_u2_down_count) + float(u1_down_u2_up_count))/float(total_value)
    return positive_part-negative_part


category = []
similarity_index = []
client = MongoClient()
db = client.mydb
content = db.links

for k in content.find():
    categ = str(k['category'])
    category.append(categ)
content = db.user_data
distinct = content.distinct("user")
total_count = len(category)


def user_similarity(user):
    temp_articles_upvote = []
    temp_articles_user_upvote = []
    temp_articles_downvote = []
    temp_articles_user_downvote = []
    sum_coefficient = float(0)
    similar_user = None
    overall_max = float(0)
    for j in distinct:
        for c in category:
            if j != user:
                for w in content.find({"user": j, "category": c, "response": "upvote"}):
                    temp_articles_upvote.append(w['article_id'])
                for w in content.find({"user": user, "category": c, "response": "upvote"}):
                    temp_articles_user_upvote.append(w['article_id'])
                for w in content.find({"user": j, "category": c, "response": "downvote"}):
                    temp_articles_downvote.append(w['article_id'])
                for w in content.find({"user": user, "category": c, "response": "downvote"}):
                    temp_articles_user_downvote.append(w['article_id'])
                sum_coefficient += coefficient(temp_articles_user_upvote,temp_articles_user_downvote,temp_articles_upvote,temp_articles_downvote)
        current_max = sum_coefficient/total_count
        if current_max > overall_max:
            overall_max = current_max
            similar_user = j

    not_read = []

    for c in category:
        article_user_temp = []
        article_similar_temp = []

        for y in content.find({"user": user, "category": c, "response": "upvote"}):
            article_user_temp.append(y['article_id'])
        for z in content.find({"user": similar_user, "category": c, "response": "upvote"}):
            article_similar_temp.append(z['article_id'])
        for art in article_similar_temp:
            if art in article_user_temp:
                pass
            else:
                post = {"category": c, "article_id": art}
                not_read.append(post)
    final_unread_category = []
    final_unread_article = []
    for var in range(0, len(not_read)):
        final_unread_category.append(not_read[var]['category'])
        final_unread_article.append(not_read[var]['article_id'])

    return final_unread_category,final_unread_article


#list_of_article, list_of_category = user_similarity("user")
#for p in range(0, len(list_of_article)):
#    path = path_finder(list_of_category[p], list_of_article[p])
#    print path


