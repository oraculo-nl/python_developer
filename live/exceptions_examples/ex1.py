try:
    x = int(input("Geef een getal: "))
# except ValueError:
#     print("Je hebt geen getal ingevoerd.")
# except ZeroDivisionError:
#     print("Je kan niet de getal 0 delen.")
# except all other errors
except Exception as e:
    print(e)
else:
    print(10 / x)
finally:
    print("bedankt voor het invoeren")

print("we gaan hier verder")