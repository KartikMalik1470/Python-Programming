try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
else: # else is for when you dont want to print the msg if exception occurs
    print("We were succesful")