class Person:
    country = "india"
    def takeBreath(Self):
        print("I am breathing.....")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so i am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"
    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        print("I am a Programmer so i am breathing++...")

p = Person()
p.takeBreath()
# print(p.company) throws an error

e = Employee()
e.takeBreath()
print(e.company)

pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)

