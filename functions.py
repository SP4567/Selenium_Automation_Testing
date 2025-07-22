#Methods or functions are a block of code that is used to execute a set of statements that perform certain tasks.
#These makes code: maintainable, reusable, easy to understand and handle, simple
def calc():
    x = int(input("Enter the 1st number: "))
    y = int(input("Enter the 2nd  number: "))
    ch = input('Enter a character: ')
    if ch == '+': print(x + y)
    elif ch == '-': print(x - y)
    elif ch == '*': print(x * y)
    elif ch == '/': print(x / y)
    elif ch == '%': print(x % y)
    else: print("Invalid Operator")
calc()

