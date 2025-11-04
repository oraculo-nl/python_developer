

temperatuur = int(input("voer een temperatuur in: "))

# controleer of getal positief, negatief of nul is
# if getal > 20:
#     print('warm')
# elif getal >10:
#     print('gematigd')
# else:
#     print('koud')


if temperatuur > 10 and temperatuur < 20:
    print('gematigd')
elif temperatuur > 20:
    print('warm')
elif temperatuur < 10:
    print('koud')

