import sys
sys.path.append('/mymodules/')
import mymodules
from mymodules.mathop import *
#this is smart calcy
print(responses[0])
print()
print(responses[4])


while True:
    print()
    text=input("What can I do for you?\nTYPE HERE:")

    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l=extract(text)
                if len(l)==2:
                    r=operations[word.upper()](l[0],l[1])
                elif len(l)==1:
                    r=operations[word.upper()](l[0])
                print(r)

            except:
                print("Something is wrong! Please Try Again\n")
            finally:
                break

        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()
            
