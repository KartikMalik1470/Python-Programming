class Employee:
    company = "Google"
    salary = 100

kartik = Employee()
anshuman = Employee()

kartik.salary = 300
anshuman.salary = 400

print(kartik.company)
print(anshuman.company)


Employee.company = "Youtube"

print(kartik.company)
print(anshuman.company)
print(kartik.salary)
print(anshuman.salary)