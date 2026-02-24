# oefening 1
# Maak een lijst met getallen van 1 t/m 10 en
# print de even getallen.

nummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for nummer in nummers:
    if nummer%2==0:
        print(nummer, end = " " )


print()




# oefening 2
# Maak een tuple met 3 steden en
# print ze netjes onder elkaar.

steden = ("barcelona", "parijs", "stockholm")

for stad in steden:
    print(stad)



# oefening 3 

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
print(set1 & set2)
