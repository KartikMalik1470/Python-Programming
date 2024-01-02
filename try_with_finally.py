try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
finally: #finally part always runs irresective of the exception
    print("We are done")