import requests
url = "https://data.buienradar.nl/2.0/feed/json"
response = requests.get(url)

# read the json data from the response into a variable
data = response.json()

metingen = data["actual"]["stationmeasurements"]

amsterdam_temp = None

for m in metingen:
    station = m.get("stationname", "").lower()
    regio = m.get("regio", "").lower()
    if "amsterdam" in station or "amsterdam" in regio:
        amsterdam_temp = m.get("temperature")
        amsterdam_time = m.get("timestamp")
        amsterdam_weather = m.get("weatherdescription")
        break

if amsterdam_temp is not None:
    print(f"De temperatuur in Amsterdam is {amsterdam_temp}°C")
    print(f"De tijd is {amsterdam_time}")
    print(f"De weer is {amsterdam_weather}")
    # print(f"Time: {amsterdam_temp['timestamp']}")
    # print(f"Weather: {amsterdam_temp['wheatherdescription']}")
else:
    temp = amsterdam_temp["temperature"]
    print("Geen meetstation voor Amsterdam gevonden in deze JSON.")

