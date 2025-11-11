import requests
import json

data = requests.get("http://api.marketstack.com/v1/eod?access_key=e6819e77d99d8ef8af384df8956b0651&symbols=MSFT")

with open('msft.json', 'w') as outfile:
    json.dump(data.json(), outfile)
