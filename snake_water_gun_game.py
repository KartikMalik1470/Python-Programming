import random

#rock paper and scissors game
def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False


print("comp turn: rock(r), paper(p) or scissors(s)?")
randno = random.randint(1,3)
if randno == 1:
    comp = 'r'
elif randno == 2:
    comp = 'p'
elif randno == 3:
    comp = 's'

you = input("your turn: rock(r), paper(p) or scissors(s)?")

a = gameWin(comp, you)

print(f"computer chose: {comp}")
print(f"you chose: {you}")

if a == None:
    print("the game is a tie")
elif a:
    print("you win")
else:
    print("you loose")


