# Werken met pathlib
from pathlib import Path

bestand = Path("voorbeeld.txt")
print("Bestandsnaam:", bestand.name)
print("Absolute pad:", bestand.resolve())
print("Bestaat:", bestand.exists())
