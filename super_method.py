# class Person:
#     country = "india"

#     def __init__(self) :
#         print("Initializing Person.....\n")

#     def takeBreath(Self):
#         print("I am breathing.....")

# class Employee(Person):
#     company = "Honda"

#     def __init__(self) -> None:
#         super().__init__()
#         print("Initializing Employee....\n")

#     def getSalary(self):
#         print(f"Salary is {self.salary}")

#     def takeBreath(self):
#         print("I am an Employee so i am luckily breathing..")

# class Programmer(Employee):
#     company = "Fiverr"
#     def __init__(self):
#         super().__init__()
#         print("Initializing Programmer....\n")

#     def getSalary(self):
#         print(f"No salary to programmers")

#     def takeBreath(self):
#         super().takeBreath()
#         print("I am a Programmer so i am breathing++...")

# p = Person()
# p.takeBreath()
# # print(p.company) throws an error

# e = Employee()
# e.takeBreath()

# pr = Programmer()
# pr.takeBreath()

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        super().speak()  # This calls the speak() method from the parent class
        print("Dog barks")

dog = Dog()
dog.speak()
