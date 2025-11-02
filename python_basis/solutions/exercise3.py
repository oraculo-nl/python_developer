leeftijd = int(input("Leeftijd: "))
if leeftijd < 12:
    print("kind")
elif leeftijd <= 17:
    print("tiener")
elif leeftijd <= 64:
    print("volwassene")
else:
    print("senior")