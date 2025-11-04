# Controleren of bestand bestaat
from pathlib import Path

pad = Path("voorbeeld.txt")
if pad.exists():
    print("Het bestand bestaat.")
else:
    print("Bestand niet gevonden.")
