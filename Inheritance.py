# class ParentClass:
#     def __init__(self):
#         print("Parent class constructor")
#     def parentFunc(self):
#         print("Parent function called")
# class ChildClass(ParentClass):
#     def __init__(self):
#         print("Child class constructor")
#     def childFunc(self):
#         print("Child function called")
# p = ParentClass()
# p.parentFunc()
# c = ChildClass()
# c.childFunc()

class SI:
    interest = 0.6
    def __init__(self, name, loan):
        self.name = name
        self.loan = loan
    def simpleInterest(self):
        return self.interest * self.loan
p1 = SI('Monica', 300000)
print(p1.simpleInterest())

class studentInterest(SI):
    rate = 0.2
    def simpleInterest(self):
        return self.rate * self.loan
p2 = studentInterest('Monica', 300000)
print(p2.simpleInterest())