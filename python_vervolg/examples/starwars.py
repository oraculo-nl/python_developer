import requests

data = requests.get("https://swapi.dev/api/people/2")

print (data.status_code)
print(data.text)
