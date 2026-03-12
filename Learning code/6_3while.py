#safe System

seceret_code="007"
code=0
#alternate of while =while(True):
while(seceret_code=="007"):
    code=input("Enter your code : ")
    if seceret_code==code:
        print("vault open")
        break
    else :
        print("Try agian")

