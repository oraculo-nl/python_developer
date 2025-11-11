import json
import matplotlib.pyplot as plt

with open('msft.json', 'r') as infile:
    data = json.load(infile)

dagen = data['data']

x = []
y = []

for dag in dagen:
    x.append(dag['date'][:10])
    y.append(dag['close'])
    print(dag['date'][:10], dag['close'] )

x.reverse()
y.reverse()

plt.plot(x, y)
plt.xticks(rotation=60)
plt.show()