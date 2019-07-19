import requests,json
from . import geo

api_key = ''
cam_key = ''

#API keys needed to be added to the api.json file values
with open('cyberapp/code/api.json') as f:
    f = json.load(f)
    weather_key = f['weather']
    cam_key = f['webcams']

'''
try:
    req = requests.get('https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'.format(geo.lat, geo.long, weather_key))
    req = req.json()
    print(req)

    wind = req['wind']['speed']
    today= req['weather'][0]['main'].title()
    humidity= req['main']['humidity']
    description ='{} with {}% Humidity. Wind speeds at {} mph.\
    '.format(req['weather'][0]['description'].title(), humidity, wind)
    kelvin = req['main']['temp']

    temp = (9/5*(kelvin - 273)) + 32 #converts to fahrenheit

    celcius = (temp-32)*5/9
    celcius='{:.2f}'.format(celcius)
    temp = '{:.2f}'.format(temp)
'''
try:
        r = requests.get("https://webcamstravel.p.rapidapi.com/webcams/list/nearby={},\
        {},100?lang=en&show=webcams%3Aimage%2Clocation".format(geo.lat,geo.long),
        headers={"X-RapidAPI-Host": "webcamstravel.p.rapidapi.com","X-RapidAPI-Key":"{}".format(cam_key)}).json()

        image = r['result']['webcams'][0]['image']['current']['thumbnail']
        title = r['result']['webcams'][0]['title'].title()

except (ConnectionError or OSError or IndexError or KeyError):
        image = ''
        title = ''
        print('Something went wrong.')
