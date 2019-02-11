responses=["Welcome to smart calculator","\nHello sir,\n","\nThanks\n","\nSorry sir! I am not understanding you\n","\nHello Lokesh! My name is Anthony! I am your smart calulator.\n"]
import math
def extract(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return(l)

def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            print("LCM is",end=' ')
            return L
        L+=1

def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            print("HCF is",end=' ')
            return H
        H-=1

def add(a,b):
    print("Addition is",end=' ')
    return a+b

def sub(a,b):
    print("Subtraction is",end=' ')
    return a-b

def multiply(a,b):
    print("Multiplication is",end=' ')
    return a*b

def power(a,b):
    print("%d to the power %d is"%(a,b),end=' ')
    return a**b

def division(a,b):
    if b==0:
        return "Infinity"
    else:
        print("Division is",end=' ')
        return a/b

def root(a):
    print("Squareroot is",end=' ')
    return math.sqrt(a)
def cuberoot(a):
    print("Cuberoot is",end=' ')
    return a**(1/3)

def fact(a):
    print("Factorial is",end=' ')
    return math.factorial(a)

def end():
    print(responses[2])
    input("Press any key to exit\n")
    exit()
def myname():
    print(responses[4])
def sorry():
    print(responses[3])
def hello():
    print(responses[1])
def intro():
    print("\nNAME: Anthony\nI am a smart Calculator\n")
    print("BIRTHDATE:21-10-2018\n")
    print("I can perform elementry mathematics operations\n")
def cool():
    print("\nThanks a lot sir!\nIt's my pleasure\n")
def thank():
    print("\nIt's my pleasure sir\n")
def morning():
    print("\nGood Morning sir! Have a nice day\n")
def night():
    print("\nGood night sir!, Sweet dreams\n")
def evening():
    print("\nGood evening Sir!\n")
def noon():
    print("\nGood noon sir\n")
def afternoon():
    print("\nGood Afternoon sir\n")
def abuse():
    print("\nKripya tameez se bat kre\n")
        
    
        
operations={"FACTORIAL":fact,"CUBEROOT":cuberoot,"SQUAREROOT":root,"UNDERROOT":root,"DIVIDE":division,"DIVISION":division,"BHAG":division,"DIVIDED":division,"POWER":power,"RAISE":power,"EXPONENT":power,"^":power,"MULTIPLY":multiply,"MULTIPLICATION":multiply,"GUNA":multiply,"INTO":multiply,"*":multiply,"+":add,"-":sub,"LCM":lcm,"HCF":hcf,"PLUS":add,"ADD":add,"ADDITION":add,"JODO":add,"JODIYE":add,"JOD":add,"SUM":add,"SUMMATION":add,"SUBTRACT":sub,"SUBTRACTION":sub,"MINUS":sub,"GHATAAO":sub,}

commands={"TATA":end,"BHAI":hello,"SMART":cool,"BRILLIANT":cool,"SUPERB":cool,"WTF":abuse,"FUCK":abuse,"BC":abuse,"CHUTIYA":abuse,"CHUTIYE":abuse,"BYE":end,"MORNING":morning,"NIGHT":night,"EVENING":evening,"AFTERNOON":afternoon,"NOON":noon,"THANK":thank,"THANKS":thank,"WOW":cool,"COOL":cool,"GREAT":cool,"IMPRESSED":cool,"NAAM":myname,"NAME":myname,"INTRO":intro,"INTRODUCTION":intro,"ABOUT":intro,"CLOSE":end,"END":end,"QUIT":end,"EXIT":end,"HELLO":hello,"HI":hello,"HEY":hello}
