from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.

import requests
import json 

def index(request):
    newsApi = NewsApiClient(api_key='28d679f9aac246078315304b2704d1d9')
    # data="https://newsapi.org/v2/everything?q=cybernews&from=2023-02-25&sortBy=publishedAt&apiKey=28d679f9aac246078315304b2704d1d9"
    # print(data)
    res = requests.get("https://newsapi.org/v2/everything?q=cybernews&from=2023-02-25&sortBy=publishedAt&apiKey=28d679f9aac246078315304b2704d1d9")
    response = json.loads(res.text)
    print(response)
    # headLines = newsApi.get_top_headlines(category='cyber')
    articles = response['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, "main/index.html", context={"mylist": mylist})