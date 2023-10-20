#Password Generator
import random

while True:
    mylist1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    mylist2=['0','1','2','3','4','5','6','7','8','9']
    mylist3=['@','#','$','*','<','>']
    password1=random.choices(mylist1, weights=None, k=int(input("enter length of password: "))-3)
    password2=random.choices(mylist2, weights=None, k=2)
    password3=random.choices(mylist3, weights=None, k=1)
    password=password1+password2+password3
    random.shuffle(password)
    # Function to convert
    def listToString(password):
 
         # initialize an empty string
          str1 = " "
 
         # return string
          return (str1.join(password))
         
    # Driver code
    print("GENERATED PASSWORD:",listToString(password))

    run = input("Press9(E/e) to exit and press(enter) to genetate a new password")
    if run.lower() == "e":
        break
    else:
       continue


