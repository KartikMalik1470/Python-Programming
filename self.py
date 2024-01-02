class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f"salary for this employee wokring in {self.company} is{self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("good morning, sir")
    
    @staticmethod
    def time():
        print("the time is 9AM in the morning")

kartik = Employee()
kartik.salary = 100000

kartik.getSalary("Thanks! ")
kartik.greet() #Employee.greet() we want to run it like this
kartik.time()
'''kartik.getSalary() gets converted to Employee.getSalary(kartik) 
that's why it throws error of no argument given'''