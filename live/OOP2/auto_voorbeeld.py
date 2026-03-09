from auto import Auto

a = Auto("Toyota")
b = Auto("BMW")
# a.merk, b.merk
autos = [a, b]


b.versnellen(200)

for auto in autos:
    if auto.get_merk() == "Toyota":
        auto.versnellen(100)
        print(auto)
    elif auto.get_merk() == "BMW":
        auto.remmen(100)
    print(auto)

print(a)