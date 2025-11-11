# Combineer datetime, random en pathlib om een log te schrijven
from datetime import datetime
import random
from pathlib import Path

logpad = Path("log.txt")
with logpad.open("a", encoding="utf-8") as f:
    f.write(f"{datetime.now().isoformat()} | value={random.random()}\n")
print("Weggeschreven naar", logpad.resolve())
