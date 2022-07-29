import random


def gameWin (comp,you):
    if comp =='s':
        if you =='w':
            return False
        elif you=='g':
            return True
    if comp =='w':
        if you =='g':
            return False
        elif you=='s':
            return True
    if comp =='g':
        if you =='s':
            return False
        elif you=='w':
            return True
         



print("comp Turn: Snake(s) Water (w) or gun (g)?")
randNo = random.randint(1,3)
print(randNo)
if randNo == 1 :
    comp='s'
elif randNo == 2:
    comp='w'
elif randNo == 3:
    comp='g'


b=input("your  Turn: Snake(s) Water (w) or gun (g)?")
a=gameWin(comp , you)

print(f"Computer Chose {comp}")
print(f"You chose{you}")
if a ==None:
    print("The game is a Tia")
elif a :
    print("You Win")





