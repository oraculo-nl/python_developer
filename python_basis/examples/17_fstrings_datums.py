# Datums formatteren in f-strings
from datetime import datetime
nu = datetime(2025, 10, 22, 14, 5, 0)
print(f"ISO: {nu:%Y-%m-%d}")
print(f"Tijd: {nu:%H:%M}")
print(f"Volledig: {nu:%A %d %B %Y}")