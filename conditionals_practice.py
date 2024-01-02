# #question number 1

# num1 = int(input("enter number 1: "))
# num2 = int(input("enter number 2: "))
# num3 = int(input("enter number 3: "))
# num4 = int(input("enter number 4: "))

# if(num1>num4):
#     f1 = num1
# else:
#     f1 = num4

# if(num2>num3):
#     f2 = num2
# else:
#     f2 = num3

# if(f1>f2):
#     print(str(f1) + " is the greatest number ")
# else:
#     print(str(f2) + " is the greatest number ")

#question number 2

# sub1 = int(input("enter the marks for 1st subject \n"))
# sub2 = int(input("enter the marks for 2st subject \n"))
# sub3 = int(input("enter the marks for 3st subject \n"))

# if(sub1<33 or sub2<33 or sub3<33):
#     print("your are fail because less than 33% in one of the subjects")

# if((sub1+sub2+sub3)/3 <40):
#     print("you are failed due to toal percentage less than 40")
# else:
#     print("congrats! you passed this exam")

#question number 3

# text = input("enter the text: \n")
# spam = False

# if("make a lot of money" in text):
#     spam = True
# elif("buy now" in text):
#     spam = True
# elif("subscribe this" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("this text is spam")
# else:
#     print("this text is not spam")


# calculator 

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))

# print("given options: add, sub, mul, div")
# choice = input("what do you want to do: \n")


# if(choice == "add"):
#     # print(f"the {choice}ition of the numbers is {a+b}")
#     print("the {}ition of the numbers is {}".format(choice,a+b))
# elif(choice == "sub"):
#     print("the {}traction of the numbers is {}".format(choice,a-b))
# elif(choice == "mul"):
#     print("the {}tiplication of the numbers is {}".format(choice,a*b))
# elif(choice == "div"):
#     print("the {}ision of the numbers is {}".format(choice,a/b))
# else:
#     print("please enter from the above given operations")


# question number 4

# username = input("enter your username: ")

# if(len(username)<10):
#     print("yes")
# else:
#     print("no")

#question number 5

# names = ["kartik", "aarushi", "sanna", "ved", "mohit"]

# name = input("enter the name to check: \n")

# if name in names:
#     print("your name is present in this list ")
# else:
#     print("your name is not present on this list ")

# question number 6

# marks = int(input("enter your marks: "))

# if(marks>=90 and marks<=100):
#     print("your rank is EX")
# if(marks>=80 and marks<=90):
#     print("your rank is A")
# if(marks>=70 and marks<=80):
#     print("your rank is B")
# if(marks>=60 and marks<=70):
#     print("your rank is C")
# if(marks>=50 and marks<=60):
#     print("your rank is D")
# if(marks<50):
#     print("your rank is F")

#leap year question
# year = int(input())
# if(year%4 == 0 and year%100 != 0 and year%400 == 0):
#     print("True")
# else:
#     print("False")

# question number 7

sentence = input("write your sentence: ")

if("harry" in sentence):
    print("yes 'harry' is present in the sentence")
else:
    print("no 'harry' isn't present in the sentence")