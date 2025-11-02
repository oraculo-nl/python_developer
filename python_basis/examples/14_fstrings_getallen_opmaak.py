# Getallen opmaken
pi = 3.1415926535
bedrag = 12345.6789

print(f"Pi op 2 decimalen: {pi:.2f}")
print(f"Bedrag met 2 decimalen: €{bedrag:.2f}")
print(f"Met duizendtalseparator: {bedrag:,.2f}")
print(f"Breedte en uitlijning: |{bedrag:>12.2f}| |{bedrag:^12.2f}| |{bedrag:<12.2f}|")