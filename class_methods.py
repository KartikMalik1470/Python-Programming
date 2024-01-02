class Employee:
    company = "Camel"
    salary = 100 #salary is a class attribute in this
    location = "Delhi"

    # def changeSalary(self, sal):
    #     self.salary = sal # this wont change the class attribute but what it will do is 
    #                       # make a new instance attribute named sal
    #     self.__class__.salary = sal # __ methods are known as dunder methods these are used to change the class attributes

    @classmethod #this method is also used to change the class attribute
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)