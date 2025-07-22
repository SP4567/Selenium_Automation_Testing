#Range is a builtin function that is used to generate the sequence of numbers
#Always takes the same amount of memory until unless we define an external list or tuples.

for i in range(10):
    print(' ', end="")
    for j in range(i):
        print(i, end=" ")
    print()