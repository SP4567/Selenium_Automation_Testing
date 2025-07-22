tup1 = (1,2,3,4)
tup2 = (4,5,6,7)
tup3 = ("Suyash", "Pandey", "Software Engineer")
tup4 = (True, False)
tup5 = (0, True, 'Hello', 25.40)
print(tup1[0])
print(tup5[3])
tup6 = tup1 + tup2
print(tup6)
print(len(tup4))
print(type(tup5))
print(tup1.count(2))
print(tup1.index(1))
for x in tup1:
    print(x)

tup7 = tup4 + tup5 + tup3 + tup2 + tup1
print(tup7[0:9])
