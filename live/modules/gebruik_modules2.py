import datetime as dt

print(dt.datetime.now())

# print formatted datetime
print(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# print day of the week
print(dt.datetime.now().strftime("%A"))

# print the milliseconds of today
print(dt.datetime.now().strftime("%f"))

import os

print(os.system("dir"))


import sys
print(sys.path)


