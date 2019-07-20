import requests, datetime,random, json

today = datetime.date.today()
news_key=''
#API keys needed to be added to the api.json file values
with open('cyberapp/code/api.json') as f:
    f = json.load(f)
    news_key = f['news']


try:

    url = ('https://newsapi.org/v2/everything?'
           'q=news english&'
           'from={}&'
           'sortBy=popularity&'
           'apiKey={}'.format(today,news_key))

    response = requests.get(url)

    r = response.json()

    articles =[]

    for x in r['articles']:
        articles.append(x)



    rand = random.randint(0,3) # generate a random number
    rand2 = random.randint(4,7)
    rand3 = random.randint(8,10)


    title= r['articles'][rand]['title'].title() #title
    published= r['articles'][rand]['publishedAt'] #published
    description= r['articles'][rand]['description'] #description
    author= r['articles'][rand]['author'] #author
    url= r['articles'][rand]['url'] #url
    image= r['articles'][rand]['urlToImage'] #image

    title2= r['articles'][rand2]['title'].title()
    published2= r['articles'][rand2]['publishedAt'] #published
    description2= r['articles'][rand2]['description'] #description
    author2= r['articles'][rand2]['author'] #author
    url2= r['articles'][rand2]['url'] #url
    image2= r['articles'][rand2]['urlToImage'] #image

    title3= r['articles'][rand3]['title'].title() #title
    published3= r['articles'][rand3]['publishedAt'] #published
    description3= r['articles'][rand3]['description'] #description
    author3= r['articles'][rand3]['author'] #author
    url3= r['articles'][rand3]['url'] #url
    image3= r['articles'][rand3]['urlToImage'] #image

except requests.exceptions.ConnectionError:
    title= None
    published= None
    description= None
    author= None
    url= None
    image = None

    title2= None
    published2= None
    description2= None
    author2= None
    url2= None
    image2 = None

    title3= None
    published3= None
    description3= None
    author3= None
    url3= None
    image3 = None
    print('Something went wrong.')
