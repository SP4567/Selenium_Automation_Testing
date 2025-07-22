print(max(10, 20, 4))
tup1 = (1,2,3,4,5,6,8)
print(max(tup1))
print(min(tup1))

i = iter(tup1)
j = reversed(tup1)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(j))
print(next(j))

x = slice(1,5,2)
print(tup1[x])

tup2 = (5,7,4,3,6,2,1,8)
z = sorted(tup2)
print(z)
print(sum(tup1), sum(tup2))



