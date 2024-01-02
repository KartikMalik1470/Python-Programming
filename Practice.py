# Question number 1
# def readFile(filename):
#     with open(filename, "r") as f:
#         print(f.read())

# readFile("1.txt")
# readFile("2.txt")
# readFile("3.txt")

# Question number 2
# l = [1,2,3,4,5,6,7,8,9,10]

# for index,item in enumerate(l):
#     if index==2 or index==4 or index==6:
#         print(index, item)    

#Question number 3
# num = int(input("Enter the number: "))

# table = [num*i for i in range(1,11)]
# print(table)

# Question number 4
# a = int(input("Enter number a: "))
# b = int(input("Enter number b: "))

# try:
#     print(a/b)
# except:
#     print("infinite")

#Question number 5
num = int(input("Enter the number: "))

table = [num * i for i in range(1, 11)]
print(table)
    
with open("tables.txt", "a") as f:
    f.write(str(table))
    print("Data written to tables.txt")
