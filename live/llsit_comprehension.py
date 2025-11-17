# # [<expressie> for  ... if  ...]
#
#
# data = list(range(10))
#
# print(data)
# resultaat = [ x*x for x in data if x % 2 == 0]
#
# print(resultaat)
getallen = list(range(101))
totaal = sum(x for x in getallen)
print(totaal)