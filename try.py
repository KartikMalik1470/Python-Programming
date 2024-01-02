while(True):
    print("Press q to quit")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try:
        a = int(a)
        if a>6:
            print("Your entered a number grater than 6")
    except Exception as e:
        print(f"your input resulted in an error: {e}")

print("Thanks for playing the game")
# when the exception in python is handled, the code flow continues without program interruption
