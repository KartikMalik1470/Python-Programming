# question number 1 to find the largest number using function
# def max(num1, num2, num3):
#     if(num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3
        
# print("the value of the maximum number is: "+ str(max(2,4,6)))

# question number 2 to convert celsius to fahrenheit


# def farh(cel):
#     return (cel *(9/5)) + 32

# c = int(input("enter the temp in celcius: "))
# f = farh(c)

# print("fahrenheit temp is: "+str(f))

# question number 3 to prevent print() function to print a new line at the end

# print("Hello", end=" ") 
# print("are", end=" ")
# print("you", end=" ")
# print("doing?", end=" ")

# question number 4 recurive function to calculate the sum of first n natural numbers
# sum(n) = sum(n-1) + n       

# n = int(input("enter the number: "))
# def sum_recursive(n):
#     if n<=0:
#         return 0
#     else:
#         return n+sum_recursive(n-1)

# sum = sum_recursive(n)

# print(f"the sum of {n} natural numbers is:" +str(sum))    

#question number 5 to print first n lines pf the without spaces star pattern

# n = int(input("enter the number of lines of pattern you want: "))
# for i in range(n):
#     print("*" * (n-i)) 

# question number 6 convert inches to centimeters

# def cm(inches):
#     return inches * 2.54

# inch = int(input("enter the length in inches: "))

# print("the length in centimeters is: "+str(cm(inch)))

# question number 7 remove a given word from the list and strip at the same time
# strip function removes extra spaces

# def remove_and_split(string, word):
#     newstr = string.replace(word, "")
#     return newstr.split()

# this = "     my name is kartik malik    "
# print(this)

# n = remove_and_split(this, "malik")

# print(n)/

#question number 8 to print multiplication table of a given number using function

# def multiplication(n):
#     for i in range(1,11):
#         print(f"{n}x{i} = {n*i}")

# n = int(input("enter the number: "))

# table = multiplication(n)
# print(table)


