# question number 1 to print multiplication table of a given number using for loop 
# num = int(input("enter the number: "))

# print("the table of {} is as follows".format(num))
# for i in range(1,11):
#     # print(str(num)+" x "+str(i)+" = "+str(i*num) )
#     print(f"{num}x{i}={num*i}")
    
#question number 2 to greet the people whose names start with 's'
# l1 = ["harry", "sohan", "sachin", "rahul"]

# for name in l1:
#     if name.startswith("s"):
#         print("hello "+ name)

#question number 3 to print multiplication table of a given number using while loop
# num = int(input("enter the number: "))

# i=1
# while i<=10:
#     print(f"{num}x{i}={num*i}")
#     i = i+1

#question number 4 if the number is prime or not
# num = int(input("enter the number: "))
# prime = True
# for i in range(2,num):
#     if(num%i == 0):
#         prime = False
#         break
# if prime:
#     print("the number is prime")
# else:
#     print("the number is not prime")

#question number 5 

#question number 6 to find factorial of a given number 
# n! = 1x2x3x4x5.......xn

# num = int(input("enter the number to find its factorial: "))
# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial*i
    
# print(f"the factorial of {num} is {factorial}")

#question number 5 to find the sum of first n natura numbers 

# num = int(input("enter the number: "))

# sum = 0
# for i in range(0, num+1):
#     sum = sum+i

# print(f"the sum of {num} natural numbers is {sum}")

#question number 7 to print the given star pattern
# n = int(input("enter the number of line you want to print: "))
# for i in range(n):
#     print(" "*(n-i-1), end="")
#     print("*"*(2*i+1), end="")
#     print(" "*(n-i-1))

#question number 8 to print the following star pattern

# n = 4

# for i in range(4):
#     print("*" * (i+1))

#question number 10 to print the multiplication tabel in reverse order

# num = int(input("enter the number: "))

# for i in range(10,0,-1):
#     print(f"{num} x {i} = {num*i}")