import requests

try:
    response = requests.get('https://api.ipify.org?format=json')
    response = response.json()

    ip = response['ip']

except KeyError:
    ip= 'Unknown'
