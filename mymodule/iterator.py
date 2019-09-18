l1 = [1, 243, 56, 34, 453, 34, 3, 3, 5, 33, '2323', 'sdfasf']
l1 = [x for x in range(1, 100) if x % 2 == 1]
l2 = iter(l1)
# print(next(l2))
# print(next(l2))
# print(next(l2))
# print(next(l2))
# print(next(l2))
# print(next(l2))
# print(next(l2))
# print(next(l2))
# print(next(l2))
# print(next(l2))
# print(next(l2))
# print(next(l2))
# print(next(l2))
# print(next(l2))
# print(next(l1))

l3 = (x for x in range(1, 100) if x % 5 == 0)


def gen1(n):
    i = 0
    while i <= n:
        if i % 3 == 0:
            yield i
            i += 1
        i += 1


l4 = gen1(100)
for l in gen1(100):
    print(l, end=" ")

