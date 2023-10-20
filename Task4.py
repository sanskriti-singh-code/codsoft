#stone_paper_scissor GAME
import random
# with computer
#taking user input
print("INSTRUCTIONS:this is case-sensitive so enter proper spelling and all in lower case.")

com_score=0
user_score=0

while (True):
 a=input("enter choice stone, paper, scissor")
 a=a.lower()
 mylist=["stone","paper","scissor"]
 b=random.choice(mylist)
 if(b==a):
    print("computer's choice: ",b)
    print("user's choice: ",a)
    print("Match Draw, Try Again!")
    com_score=com_score+0; user_score=user_score+0
    #wrong choice
 elif(a!="paper"and a!="scissor"and a!="stone"):
    print("Wrong choice")
    continue
 #computer chooses a stone.
 elif(b=="stone"):
    print("computer's choice: ",b)
    print("user's choice: ",a)
    if(a=="scissor"):
        print("oops! You loose -You're hit by a stone!")
        com_score=com_score+1
        user_score=user_score+0
    else:
        print("Wohooo! You Won-you Trapped a stone!")
        com_score=com_score+0
        user_score=user_score+1
   
#computer chooses a paper.
 elif(b=="paper"):
    print("computer's choice: ",b)
    print("user's choice: ",a)
    if(a=="stone"):
        print("oops! You loose -You're Trapped by a paper!")
        com_score=com_score+1
        user_score=user_score+0
    else:
        print("Wohooo! You Won- Paper turned into pieces!")   
        com_score=com_score+0
        user_score=user_score+1
   
#computer chooses a scissor.

 elif(b=="scissor"):
    print("computer's choice: ",b)
    print("user's choice: ",a)
    if(a=="paper"):
        print("oops! You loose -Paper turned into pieces!")
        com_score=com_score+1
        user_score=user_score+0
    else:
        print("Wohooo! You Won-scissor is damaged!") 
        com_score=com_score+0
        user_score=user_score+1
   
   
 run = input("Press9(E/e) to exit game and press(enter) to continue")
 if run.lower() == "e":
        break
 else:
    continue
print("computer's score",com_score)
print("your's score",user_score)
if(com_score>user_score):
   print("Oops! you loose..")
elif(com_score<user_score):
   print("Wohooo! YOU WON THE GAME")
else:
   print("Match Draw")

