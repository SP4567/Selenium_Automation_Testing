dict1 = {1:1, 2:4, 3:9, 4:16, 5:25}
print(dict1)
dict2 = {1:"Suyash", 2:"Monica"}
dict3 = {'1st':"Suyash", '2nd':"Monica"}
print(dict1, dict2, dict3)
print(dict1[1], dict2[2], dict3['1st'])
dict3['3rd'] = 'Loves'
print(dict1, dict2, dict3)
dict3.pop('3rd')
print(dict1, dict2, dict3)
print(dict1.get(1))
print(dict2.keys())
print(dict3.items())
print(dict1.keys(), dict1.values())
print(dict1.pop(5))
print(dict1.popitem())
print(dict1.update({4:16}))
print(dict1)
dict_ = dict1.copy()
print(dict_)
dict3.clear()
print(dict3)