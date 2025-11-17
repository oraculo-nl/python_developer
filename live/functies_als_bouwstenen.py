# def greet(name):
#     return f"Hello, {name}!"
#
#
# bericht = greet("Bob")
#
# print(bericht)


# def apply_twice(f, value):
#     uitkomst = f(value)
#     return uitkomst
#
# apply_twice(print, "python")

# square = lambda x: x * x
#
# print(apply_twice(square,2))

# words = ["apple", "pear", "banana"]
# words.sort(key=lambda w: len(w))
# print(words)

from functools import reduce

numbers = list(range(101))
f = lambda x: x*x
f2 = lambda x: x%2==0
f3 = lambda x,y: x+y
# squares = list(map(f, numbers))
# even_getallen = list(filter(f2, numbers))
totaal = reduce(f3, numbers)
print(numbers)
print(totaal)
# print(numbers)
# print(squares)
# print(even_getallen)

