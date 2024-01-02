class Employee:
    company = "Visa"
    ecode = 1234

class Freelancer:
    company = "SEO"
    level = 2

    def upgradeLevel(self):
        self.level = self.level+1

class Programmer(Employee, Freelancer):
    name = "Kartik"

p = Programmer()

p.upgradeLevel()
print(p.level)
print(p.company)