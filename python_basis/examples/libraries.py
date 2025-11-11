
from datetime import datetime
import random, pathlib

logpad = pathlib.Path("log.txt")

with logpad.open("a") as f:
    f.write(f"{datetime.now()}: {random.random()}\n")