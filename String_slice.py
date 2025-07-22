s = "Welcome to ChatGPT, the world of AI"
print(s[0:10])
print(s[0:11:1])
print(s[0])
print(s[1])
print(s[3:])


st = s[::-1]
if s == st:print ("Palindrome")
else:
    print("Not Palindrome")


y = "name, age, gender"
print(y.index(','))
print(y[0:y.index(',')])