import nltk, string
import scipy
from sklearn.feature_extraction.text import TfidfVectorizer
from file_count import file_count
from pymongo import MongoClient

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)


def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''


def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')


def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0, 1]


def get_similarity(text1, text2):
    return cosine_sim(text1, text2)


def similarity_list(folder):
    it = file_count(folder)
    i = 1
    client = MongoClient()
    db = client.mydb
    content = db.meta_data
    while i < it:
        x = open('C:/zeus/' + folder + '/' + str(i) + '.txt', 'r')
        article1 = x.read()
        list1 = []
        list2 = []
        j = 1
        while j < it:
            f = open('C:/zeus/' + folder + '/' + str(j) + '.txt', 'r')
            article2 = f.read()
            value = get_similarity(article1, article2)
            list1.append(value)
            list2.append(j)
            print i, value
            j += 1
        article_check = content.find({"article_id": i, "category": folder})
        if article_check.count() != 0:
            content.remove({"article_id": i, "category": folder})
        list1, list2 = zip(*sorted(zip(list1, list2), reverse=True))
        post = {"category": folder,
                "article_id": i,
                "similar_to": list2,
                "upvotes": 0,
                "downvotes": 0}
        i += 1
        content.insert_one(post)
