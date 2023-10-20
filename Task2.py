#calculator
import math

while (True):
    a=int(input("enter 1st no."))
    b=int(input("enter 2nd no."))
    c=input("enter operator from(+,-,*,^,/,%,//)")

    if(c=="+"):
      ans=a+b
      print("sum= ",ans)

    elif(c=="-"):
      ans=a-b
      print("subtract= ",ans)

    elif(c=="*"):
      ans=a*b
      print("Multiply= ",ans)

    elif(c=="^"):
      ans=math.pow(a,b)
      print("power= ",ans)

    elif(c=="%"):
        ans=a%b
        print("modulus= ",ans)

    elif(c=="/"):
      ans=a/b
      print("Integer_division= ",ans)

    else:
       ans=a//b
       print("Division= ",ans)
    run = input("Press(E/e) to exit and press(enter) to continue")
    if run.lower() == "e":
        break
    else:
       continue