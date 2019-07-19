import requests

try:
    response = requests.get('https://api.ipify.org?format=json')
    response = response.json()

    ip = response['ip']

except(ConnectionError or OSError or IndexError or KeyError):
    ip= '8.8.8.8'

try:
    alt = requests.get('https://api.ipgeolocationapi.com/geolocate/{}'.format(ip)).json()

    lat = alt['geo']['latitude']
    long = alt['geo']['longitude']

except(ConnectionError or OSError or IndexError or KeyError):
    lat= 0
    long = 0
    print('Something went wrong.')
