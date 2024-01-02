try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(f"The value of c is {c}")
    print(type(c))

#handling different exceptions in different ways
except ValueError as v:
    print("Exception 1 occured")
    print(v)

except ZeroDivisionError as z:
    print("Exception 2 occured")
    print(z)

print("Thanks for using this code!")