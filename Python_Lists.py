x = [1, 2, 3]
y = [4, 5, 6]
z = ['suyash', 'monica', 6, 22]
print(x[1:2])
print(x, y, z)
print(type(z))
print(z[0:11:2])
print(len(z))
x.append(4)
print(x)

city = ['Lucknow', 'Mathura', 'Vrindavan', 'Barsana', 'Kashi']
city.insert(0, 'Noida')
print(city)
city.remove('Noida')
print(city)
city.pop(0)
print(city)
print(city.index('Kashi'))
print(city.count("Mathura"))
city.sort()
print(city)
city.reverse()
print(city)
