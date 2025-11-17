# nums = list(range(10))
#
# it = iter(nums)
#
#
# print(next(it))
# print(next(it))

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# for n in count_up_to(100):
#     print(n)

g = count_up_to(10)

# print(next(g))
# print(next(g))
# from itertools import islice
import itertools
# print(list(islice(g,5)))

naturals = (n for n in itertools.count(0))

print(list(itertools.islice(naturals,10)))