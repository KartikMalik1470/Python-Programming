# question 1
# class Programmer:
#     company = "Microsoft"
#     def __init__(self, name, product):
#         self.name = name
#         self.product = product

#     def getInfo(self):
#         print(f"the name of the {self.company} progammer is {self.name} and the product is {self.product}")

# kartik = Programmer("Kartik", "skype")
# anshuman = Programmer("anshuman", "Github")

# kartik.getInfo()
# anshuman.getInfo()

#question 2
# class calculator:
#     def __init__(self, num):
#         self.number = num
#     def square(self):
#         print(f"the value of {self.number} square is {self.number **2}")
#     def cube(self):
#         print(f"the value of {self.number} cube is {self.number **3}")
#     def squareRoot(self):
#         print(f"the value of {self.number} squareRoot is {self.number **0.5}")

# n = int(input("enter the number: "))
# a = calculator(n)
# a.square()
# a.cube()
# a.squareRoot()

#question 3

# class Sample:
#     a = "Kartik" #this is a class attribute

# obj = Sample()
# obj.a = "Malik" #new instance attribute is created
# # Sample.a = "Malik" #now the class attribute will change
# print(Sample.a)
# print(obj.a)


#question 4
# class calculator:
#     def __init__(self, num):
#         self.number = num
#     def square(self):
#         print(f"the value of {self.number} square is {self.number **2}")
#     def cube(self):
#         print(f"the value of {self.number} cube is {self.number **3}")
#     def squareRoot(self):
#         print(f"the value of {self.number} squareRoot is {self.number **0.5}")
#     @staticmethod
#     def greet(): # we dont need self attribute in a static method it will run very first
#         print("******Hello, welcome to my calculator******")

# n = int(input("enter the number: "))
# a = calculator(n)
# a.greet()
# a.square()
# a.cube()
# a.squareRoot()

#question 5
''' let say there are 1, 2, 3, 4, 5, 6, 7
we will give seats to customer from 7 to 1 
'''
# class Train:
#     def __init__(self, name, fare, seats):
#         self.name = name
#         self.fare = fare
#         self.seats = seats

#     def getStatus(self):
#         print("******************")
#         print(f"The name of the train is {self.name}")
#         print(f"the seats available in this train are: {self.seats}")
#         print("******************")

#     def fareInfo(self):
#         print(f"the price of the ticket is: Rs.{self.fare}")
#         print("******************")

#     def bookTicket(self):
#         if(self.seats>0):
#             print(f"your ticket has been booked! your seat number is {self.seats}")
#             self.seats = self.seats - 1
#         else:
#             print("Sorry this train is full, kindly try in tatkal")
#         print("******************")

#     def cancelTicket(self, seatNo):
#         pass

# intercity = Train("intercity express: 14045", 90, 300) # an object is formed with 3 attributes

# #now runnning all the methods
# intercity.getStatus()
# intercity.bookTicket()
# intercity.getStatus()

#question 6

# class Sample:
#     a = "Kartik" #this is a class attribute
#     def __init__(Kartik, name):
#         Kartik.name = name #changing the 'self' name dosent change anything it's justa a parameter

# obj = Sample("Kartik")
# print(obj.name)

