list1 = ['India', 'USA', 'Australia', 'UK']
list2 = ['Delhi', 'WDC', 'Canberra', 'London']
s = zip(list1, list2)
print(list(s))

for x, y in zip(list1, list2):
    print(x, y)

total_cost = [10, 20, 30, 40, 50]
sale_price = [15, 25, 35, 45, 55]
for i, j in zip(total_cost, sale_price):
    print(j - i)

#Used for mapping the values from one list to another or tuples, set to set, etc. Basically ist takes two of these stuff(tuple, lists, sets) into its single stuff by mapping one over the other.