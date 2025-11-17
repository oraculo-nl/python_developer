getallen = [n for n in range(1,11)]

print(getallen)
oneven_getallen = list(filter(lambda n: n % 2 != 0,getallen))
print(oneven_getallen)
print(list(map(lambda n: n * n ,oneven_getallen)))

# oneven_getallen2 = []
#
# for i in oneven_getallen:
#     if i % 2 != 0:
#         oneven_getallen2.append(i)
#
# print("oneven_getallen2:", oneven_getallen2)

11:30