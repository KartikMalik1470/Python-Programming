class Employee:
    company = "Google"

    def showDetails(self):
        print("this is an employee")

# now making a child/derived class programmer from the parent/base class Employee
class Prorgammer(Employee):
    company = "Youtube"
    language = "Python"
    def getLanguage(self):
        print(f"The language is {self.language}")
    #overriding the showdetails method ->
    def showDetails(self):
        print("this is an programmer")


e = Employee()
p = Prorgammer()

e.showDetails()
p.showDetails() # because Programmer class has all the attributes of Employee class
print(e.company)
print(p.company)