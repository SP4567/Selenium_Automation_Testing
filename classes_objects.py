# class AreaRectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.height * self.width
#
# area = AreaRectangle(100, 100)
# print(area.area())

class Employee:
    def __init__(self, fname, lname, email, position):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.position = position
    def salaryEmployee(self):
        DA = 12000000
        TA = 10000
        HRA = 1000
        salary = DA + TA + HRA
        print("Name: ", self.fname, "", self.lname, "Email is: ", self.email, " Position: ", self.position)
        print('Salary of the employee is: ', salary)

Emp = Employee("Suyash", "Pandey", "suyashpandey9611@gmail.com", 1)
print(Emp.salaryEmployee())