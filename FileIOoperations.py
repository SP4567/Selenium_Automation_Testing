f = open('writedemo.txt', 'w')
f.write("Hello this is file handling using python! \n")
f.close()

f = open('writedemo.txt', 'a')
l  =[1,2,3,4,5,6]
for i in l:
    f.write(str(i))
f.close()

f = open('writedemo.txt', 'r')
print(f.read())

with open('writedemo.txt', 'r') as f:
    print(f.read())

with open('writedemo.txt', 'a') as f:
    f.write("\nHello, this is Suyash Pandey, software engineer!")
    f.close()