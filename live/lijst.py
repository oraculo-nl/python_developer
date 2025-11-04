fruits = ["appel", "banaan", "kers"]

# print(fruits[1])
# fruits.append("mango")
# fruits.insert(1,"peer")
# print(fruits)
# print(fruits.index("banaan"))
index = fruits.index("banaan")
print(index)
print(fruits[index])
element = fruits[index]
fruits.remove(element)
print(fruits)
