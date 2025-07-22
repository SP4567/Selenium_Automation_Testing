x = 40 #global vairable, as this can be used in any function. Not declared inside any specific function.
def demo():
    global x #if global keyword is written with a variable then it becomes the global variable.
    x = 20 # local variable, as its usage is within the function only not outside the function or in any other
    # function outside this function.
    print(x)
demo()

def demo1():
    print(x) #global scope
demo1()

def dem(): # enclosing scope, scope within the scope of another function.
    i = 20
    print(i)
    def den():
        print(i)
    den()
dem()

j = 5
def dem1():
    j = 10
    print(j)
    def dem2():
        j = 20
        print(j)
        def dem3():
            j = 30
            print(j)
            def dem4():
                j = 40
                print(j)
            dem4()
        dem3()
    dem2()
dem1()

