# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
# import cmath

# a = int(input("enter a:"))
# b = int(input("enter b:"))
# c = int(input("enter c:"))

# # calculate the discriminant
# d = (b**2) - (4*a*c)

# # find two solutions
# sol1 = (-b-cmath.sqrt(d))/(2*a)
# sol2 = (-b+cmath.sqrt(d))/(2*a)

# print(f"The solution are {sol1} and {sol2}")

# num = int(input(" enter the number:"))
# if(num%2 == 0):
#     print("number is even")
# else:
#     print("the number is odd")
# if(num > 0 ):
#     print("the number is positive")
# elif(num < 0):
#     print("the number is negative")
# else:
#     print("the number is zero")



# for i in range(1, 100):
#     if ()
#             print(i)
#         else:
            

# num = int(input("give a number: "))

# if num > 1:
#     for i in range(2,num):
#         if (num%i == 0):
#             print("Its not a prime number")
#             break
#         else:
#             print("its not a prime number")
#             break

# print("the list of prime numbers between 1-10000 is: ")

# for num in range(2, 10001):
#     prime = True
#     if num <=1:
#         prime = False
#     else:
#         prime = True
    
# for i in range(2, 11):
#     for j in range(2,11):
#         if j%i 
    
for i in range(2, 10001):
    is_prime = True  # Assume i is prime until proven otherwise
    for j in range(2, i):
        if i % j == 0:
            is_prime = False  # i is divisible by j, so it's not prime
            break  # No need to check further, exit the inner loop
    if is_prime:
        print(i , end=",")

