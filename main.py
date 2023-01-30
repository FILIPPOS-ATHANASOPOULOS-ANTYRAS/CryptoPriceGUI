
import pprint
import requests
import json

key = '003bcfd0-12b8-4c46-a494-086572b4f4aa'

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

params = {
    'slug' : 'bitcoin',
    'convert' : 'USD'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': key
}

def getPrice():
    result = requests.get(url,params = params , headers = headers).json()
    price = result['data']['1']['quote']['USD']['price']
    return price


