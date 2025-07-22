try:
    print("Input 1st Number: ")
    x = int(input())
    print("Input 2nd Number: ")
    y = int(input())
    print(x / y)
    print("Executed")
except Exception as e:
    print(e)
    print("In except block")
# else:
#     print("In else")
finally: print("Finally always executes")