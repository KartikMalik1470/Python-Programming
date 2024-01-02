# Question number 1
# class C2DVec:
#     def __init__(self, i, j):
#         self.icap = i
#         self.jcap = j
    
#     def __str__(self):
#         return(f"{self.icap}i + {self.jcap}j")

# class C3DVec(C2DVec):
#     def __init__ (self, i, j, k):
#         super().__init__(i,j)
#         self.kcap = k

#     def __str__(self):
#         return(f"{self.icap}i + {self.jcap}j + {self.kcap}k)")

# v2d = C2DVec(1,3)
# v3d = C3DVec(1, 9, 7)

# print(v2d)
# print(v3d)/

# Question number 2

# class Animals:
#     animalType = "Mammal"

# class Pets(Animals):
#     color = "White"

# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print("bhow bhow!")

# d = Dog()
# d.bark()

# Question number 3
# salaryAfterINcrement = salary*increment
# class Employee:
#     salary = 1000
#     increment = 1.5

#     @property
#     def salaryAfterIncrement(self):
#         return self.salary*self.increment
    
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, sai):
#         self.increment = sai/self.salary

# e = Employee()
# print(e.salaryAfterIncrement)

# print(e.increment)
# e.salaryAfterIncrement = 150000 # after running this setter the increment value will change acc to the formulae
# print(e.increment)

# Question number 4
# formulae is (a+bi)(c+di) = (ac-bd) + (ad+bc)i
# class Complex:
#     def __init__(self, r, i):
#         self.real = r
#         self.imaginary = i

#     def __add__(self, c):
#         return Complex(self.real + c.real, self.imaginary + c.imaginary)
    
#     def __mul__(self, c):
#         mulReal = self.real*c.real - self.imaginary*c.imaginary
#         mulImg = self.real*c.imaginary + self.imaginary*c.real
#         return Complex(mulReal, mulImg)
    
#     def __str__(self):
#         if self.imaginary<0:
#             return (f"{self.real} - {-self.imaginary}i")
#         else: 
#             return (f"{self.real} + {self.imaginary}i")

# c1 = Complex(1, -4)
# c2 = Complex(331, -37)
# sum = c1 + c2
# mul = c1 * c2
# print(sum)
# print(mul)

#Question Number 5
# class Vector:
#     def __init__(self, vec):
#         self.vec = vec

#     def __str__(self):
#         str1 = ""
#         index = 0
#         for i in self.vec:
#             str1 += (f" {i}a{index} +")
#             index += 1
        
#         return str1[:-1] # string slicing for avoiding the end wala +
    
#     def __add__(self, vec2):
#         newList = []
#         for i in range(len(self.vec)):
#             newList.append(self.vec[i] + vec2.vec[i])

#         return Vector(newList)
    
#     def __mul__(self, vec2):
#         sum = 1
#         for i in range(len(self.vec)):
#             sum += (self.vec[i] * vec2.vec[i])

#         return sum


# v1 = Vector([1, 4, 5])
# v2 = Vector([1, 6, 7])
# print(v1+v2)
# print(v1*v2)

# Question Number 6

# Question Number 7
# class Vector:
#     def __init__(self, vec):
#         self.vec = vec

#     def __str__(self):
#         str1 = ""
#         index = 0
#         for i in self.vec:
#             str1 += (f" {i}a{index} +")
#             index += 1
        
#         return str1[:-1] # string slicing for avoiding the end wala +
    
#     def __add__(self, vec2):
#         newList = []
#         for i in range(len(self.vec)):
#             newList.append(self.vec[i] + vec2.vec[i])

#         return Vector(newList)
    
#     def __mul__(self, vec2):
#         sum = 1
#         for i in range(len(self.vec)):
#             sum += (self.vec[i] * vec2.vec[i])

#         return sum
    
#     def __len__(self):
#         return len(self.vec)


# v1 = Vector([1, 4, 5, 5, 3, 7, 8])
# v2 = Vector([1, 6, 7])
# print(len(v1))
# print(len(v2))