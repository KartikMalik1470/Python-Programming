class Employee:
    company = "bharat gas"
    salary = 5500
    salarybonus = 500
    # totalSalary = 6000 # this is known as hard coding

    @property #this is nothing but the getter method
    def totalSalary(self):
        return self.salary + self.salarybonus
    
    @totalSalary.setter
    def totalSalary(self, val):
        salarybonus = val - self.salary
    
e = Employee()
print(e.totalSalary)
e.totalSalary = 5800
print(e.salarybonus)
print(e.salary)