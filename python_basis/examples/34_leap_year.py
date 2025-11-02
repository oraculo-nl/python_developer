# Schrikkeljaar: deelbaar door 4 en niet door 100, tenzij ook door 400
jaar = int(input("Jaar: "))
is_leap = (jaar % 4 == 0) and (jaar % 100 != 0 or jaar % 400 == 0)
if is_leap:
    print(f"{jaar} is een schrikkeljaar")
else:
    print(f"{jaar} is geen schrikkeljaar")
