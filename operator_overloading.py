class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("lets Add: ")
        return self.num + num2.num
    
    def __mul__(self, num2):
        print("lets Multiply: ")
        return self.num * num2.num
    
    def __truediv__(self, num2):
        print("lets divide: ")
        return self.num / num2.num

n1 = Number(6) #n1 is a number object
n2 = Number(4)
sum = n1+n2
mul = n1*n2
div = n1/n2
print(sum)
print(mul)
print(div)