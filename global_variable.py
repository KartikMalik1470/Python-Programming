a = 54 # global variable
def func1():
    global a # this signifies that dont make another vairable and use this global a(global variable) only
    print(f"Print statement 1: {a}")
    a=8 #local variable ig global keyword is not used
    print(f"Print statement 2: {a}")

func1()
print(f"Print statement 3: {a}")