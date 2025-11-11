import requests

r = requests.get("https://api.github.com/1")

print(r.status_code)