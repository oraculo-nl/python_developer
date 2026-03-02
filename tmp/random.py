import random
import math
import datetime
import os
from pathlib import Path
import sys
import json






print(sys.path)

pad = Path("text.txt")

if pad.exists():
    print("bestand bestaat")
else:
    print("bestand bestaat niet")




print (os.system("dir"))


for i in range(10):
    print(random.randint(1,10))


print(math.pi)


# print the day of the week
print(datetime.datetime.now().strftime("%A"))
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


lijst = [1,2,3,]
d = {1:1, 2:2}
print(json.dumps("lijst"))
print(json.dumps(d))