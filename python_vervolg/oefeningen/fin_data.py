# Oefening: JSON-beursdata visualiseren met matplotlib

# -> maak een bestand get_fin_data.py
# -> lees de financiele data uit via marketstack.com
# -> gebruik json library om de data naar een .json file weg te schrijven


# -> maak een nieuwe bestand genaamd show_fin_data.py
# -> 1. Open het .json-bestand met de json-module (bijv. json.load)
# De JSON-data ziet er zo uit:
# {
#   "pagination": {...},
#   "data": [ {...}, {...}, {...} ]
# }
# 'data' is een lijst van dagen met informatie over de beurskoers.

# Voorbeeld van één dag:
# {
#   "date": "2025-11-07T00:00:00+0000",
#   "open": 267.9,
#   "high": 269.5,
#   "low": 267.2,
#   "close": 268.47,
#   ...
# }

# -> 2. Haal de lijst met dagen op uit de JSON met:
#    dagen = data['data']

# -> 3. Loop over de lijst en print per dag de datum en de slotkoers ('close'):
#    print(dag['date'], dag['close'])
# Verwachte output:
# 2025-11-07T00:00:00+0000 268.47
# 2025-11-06T00:00:00+0000 269.77
# 2025-11-05T00:00:00+0000 270.14

# -> 4. Maak twee lege lijsten vóór de loop:
#    days = []
#    prices = []

# -> 5. In de loop:
#      - Voeg de datum toe aan days (alleen de eerste 10 tekens, dus zonder tijd: [:10])
#      - Voeg de slotkoers toe aan prices

# -> 6. Visualiseer de data:
#    - Gebruik plt.plot(days, prices)
#    - Roteer de datums 60 graden met plt.xticks(rotation=60)
#    - Voeg eventueel een titel en labels toe

# -> 7. Draai de volgorde van days en prices om (zodat oudste datum links staat):
#    days.reverse()
#    prices.reverse()

