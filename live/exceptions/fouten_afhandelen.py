try:
    x = input("Geef een getal: ")

    if x == "noodsituatie":
        raise TypeError("verdubbel verwacht een getal")
    while x == "0" or not x.isdigit() :
        print("verkeerde waarde ingevoerd het moet een geheel getal zijn of niet 0")
        x = input("Geef een getal: ")

    print(10 / int(x))
except Exception as e:
    print(e)
else:
    print("OK")
finally:
    print("bedankt voor het invoeren")

# print("we gaan hier verder")

