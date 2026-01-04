'''
1 is for rock
-1 is for paper
0 is for scissors
'''
import random

computer = random.choice([1, 0, -1])
youstr = input("Enter your choice: ")
youdict = {"r":1, "p":-1, "s":0}
reversedict = {1:"rock", -1:"paper", 0:"scissors"}

you = youdict[youstr]

print(f"You choose {reversedict[you]}\n computer choose {reversedict[computer]}")

if(computer == you):
    print("Match draw")

else:
    if(computer==1 and you == -1):
        print("You win!")

    elif(computer==1 and you==0):
        print("You lose!")

    elif(computer==-1 and you==1):
        print("You lose!")

    elif(computer==-1 and you==0):
        print("You win!")

    elif(computer==0 and you==1):
        print("You win!")

    elif(computer==0 and you==-1):
        print("You lose!")
    
    else:
        print("Something went wrong!")