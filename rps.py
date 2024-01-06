import random
import time

print("...Welcome to the Game...\n")
n=input("Enter your Name:")
print("* ROUND 1 *")
l=["Rock","Paper","Scissor"]
comp_f=0
ply_f=0
tie=0
def rounds(l,n):
    global comp_f,ply_f,tie
    a=int(input("Your Choose Rock,Paper or Scissor(1,2,3):"))
    if (a==1):
        cho="Rock"
    elif (a==2):
        cho="Paper"
    elif (a==3):
        cho="Scissor"
    else:
        print("Invalid choice")

    print("Results...\n",)
    time.sleep(2)
    comp=random.choice(l)
    print("Your Choice:",cho,"\nComputer Choice:",comp,"\n")
    if (comp==cho):
        print("Tie")
        tie+=1
    if ((comp=="Rock" and cho=="Scissor") or (comp=="Paper" and cho=="Rock") or (comp=="Scissor" and cho=="Paper")):
        print("Computer Winner")
        comp_f+=1
    if ((cho=="Rock" and comp=="Scissor") or (cho=="Paper" and comp=="Rock") or (cho=="Scissor" and comp=="Paper")):
        print(n," is Winner.")
        ply_f+=1
    ask=input("\nDo you Wanna Play Again?(y/n):")
    if (ask.upper()== "Y"):
        print("\n* Next ROUND *")
        rounds(l,n)
    else:
        print(f"\n SCOREBOARD \nTie:{tie}\n{n} Score:{ply_f}\nComputer Score:{comp_f}\n")
        if (comp_f>ply_f):
            print("Computer Winner")
        elif (comp_f<ply_f):
            print(f"{n} is the Winner")
        else:
            print("It's a Tie")
        print("Thank You")
rounds(l,n)

