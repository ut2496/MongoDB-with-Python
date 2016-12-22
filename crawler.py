import requests
from bs4 import BeautifulSoup
from readability import ParserClient
import re
import os
from Insertion_to_databse import insertion
from file_count import file_count


def generate_content(url,category):
    str_article_title = "Default title"
    image_url=""
    parser_client = ParserClient(token='7c8daeedd7726bf0c7d6b042098ee320ae336d87')
    parser_response = parser_client.get_article(str(url))
    article = parser_response.json()
    str_article_title = article['title']
    strarticle = article['content']
    image_url = article['lead_image_url']
    final_article = re.sub('<.*?>', '', strarticle)
    final_article2 = re.sub('&.*?;', '', final_article)

    line = re.sub('["]', '', final_article2)
    final_article3=line.encode('utf-8').strip()
    final_article3=os.linesep.join([s for s in final_article3.splitlines() if s])
    final_article4=re.sub(' +', ' ', final_article3)
    linet=re.sub('["]', '', str_article_title)
    final_article_title = linet.encode('utf-8').strip()
    print(url)
    print (image_url)
    print(final_article4)
    insertion(category, url, final_article4, str_article_title, image_url)


def crawl_google_news(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")

    mylist = []
    for k in soup.findAll('a', {'target': '_blank'}):
        href = k.get('href')
        strhref = str(href)
        mylist.append(strhref)
    final=[]
    for i in range(0, len(mylist)):
        if mylist[i] == "None":
            var = mylist[i - 1]
        else:
            var = mylist[i]

        final.append(var)
    return final


def crawl(links,category):
    print("Generating Links")
    try:
        for p in range(0, len(links)):
            init_count = file_count(category[p])
            print("Fetching "+links[p])
            url = str(links[p])
            final = crawl_google_news(url)
            print(final)
            for j in range(0, len(final)):
                print("NEXT HERE\n")
                generate_content(final[j], category[p])
                final_count = file_count(category[p])
                if final_count-init_count == 40:
                    break
    except:
        pass


