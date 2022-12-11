# to roll dice
import random
print("Game rules:")
print("0- To exit from game\n1-6:u can choose any out of these\nothers numbers are invalid")
print()
count=0
def roll_dice(n):
    if n==0:
        print("Thank for visting")
        print("You won",count,"times")
    elif n>=1 and n<=6:
        return dice(n)
    else:
        print(" Please enter a valid number")
        return input_fun()
def input_fun():
    n=int(input('Enter a number: '))
    return roll_dice(n)
def dice(n):
    a=random.randint(1,6)
    global count
    if a==n:
        print("you are won.")
        count+=1
    else:
        print(f"{a} Better luck next time")
    input_fun()
input_fun()
