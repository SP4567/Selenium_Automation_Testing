def function(x, y): # variables passed through the function while function creation are called as the parameters.
    sum = x + y
    return sum
print(function(6, 10)) # values passed to the functions while function call are called as the arguments.

def func(str, age):
    # def func(str = 'Suyash', agr = 22): if I do like this then it will be optional arguments and in this case ot is not required to pass arguments in the function call as its optional.
    print("Name is: ", str, ", age is: ", age)
func('Suyash', 22) # this simply means if we swap the positions of the arguments, it will show an error, hence these are called as the positional arguments.
# At the same time, these are required arguments because parameters are passed through the function and hence while function call arguments are necessary too.

def add(x=11, y=12):
    return x + y
print(add(y=14))# this becomes keyword argument, when we specify it in the argument while function call.