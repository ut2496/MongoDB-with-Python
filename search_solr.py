import solr


def search(keyword,value):
    s = solr.Solr("http://localhost:8983/solr/trial")
    response = s.select(keyword + ':' + value)
    for i in response.results:
        print i


#search("title", "Syria rebels")
