class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("lets Add: ")
        return self.num + num2.num
    
    def __mul__(self, num2):
        print("lets Multiply: ")
        return self.num * num2.num
    
    def __str__(self):
        return(f"Decimal Number: {self.num}")


n = Number(9)
print(n)