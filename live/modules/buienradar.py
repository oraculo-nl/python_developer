# load the json data from the buienradar api which is located at https://data.buienradar.nl/2.0/feed/json

import requests
url = "https://data.buienradar.nl/2.0/feed/json"
response = requests.get(url)

# read the json data from the response into a variable
data = response.json()

# import json
#
# with open("live/modules/weerdata.json", "r", encoding="utf-8") as f:
#     data = json.load(f)

stations = data["actual"]["stationmeasurements"]

amsterdam = next(
    (s for s in stations if s.get("regio", "").strip().lower() == "lelystad"),
    None,
)

if amsterdam is None:
    print("Amsterdam niet gevonden in stationmeasurements.")
else:
    temp = amsterdam["temperature"]
    print(f"Temperature in Amsterdam: {temp}°C")
    print(f"Time: {amsterdam['timestamp']}")
    print(f"Weather: {amsterdam['weatherdescription']}")


