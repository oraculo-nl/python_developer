import requests

api_key=0
ticker = input("Voer de ticker in van het bedrijf:")

data = requests.get("https://api.marketstack.com/v2/eod?access_key="+api_key+"sumbols="+ticker)

with open("aapl.txt", "w", newline="", encoding="utf-8") as f:
    f.write(data.text)