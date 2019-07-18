import requests, datetime,random

today = datetime.date.today()

try:

    url = ('https://newsapi.org/v2/everything?'
           'q=news english&'
           'from={}&'
           'sortBy=popularity&'
           'apiKey=cb8a86eb77ea4d76bb86422552b2e732'.format(today))

    response = requests.get(url)

    r = response.json()

    articles =[]

    for x in r['articles']:
        articles.append(x)



    rand = random.randint(0,(int(len(articles)/2)-1)) # generate a random number

    title= r['articles'][rand]['title'].title() #title
    published= r['articles'][rand]['publishedAt'] #published
    description= r['articles'][rand]['description'] #description
    author= r['articles'][rand]['author'] #author
    url= r['articles'][rand]['url'] #url
    image= r['articles'][rand]['urlToImage'] #image

except ConnectionError:
    title= None
    published= None
    description= None
    author= None
    url= None
    image = None
