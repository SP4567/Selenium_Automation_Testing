set1 = {0,1,2,3,4}
set2 = {4,5,6,7,8,9,10,11}
set1.add(5)
print(set1)

set1.add(6)
print(set1)

set1.remove(6)
print(set1)

set1.discard(5)
print(set1)

set1.pop()
print(set1)

# set1.clear()
# print(set1)

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1.difference_update(set2))

print(set1.issubset(set2))
print(set1.issuperset(set2))

