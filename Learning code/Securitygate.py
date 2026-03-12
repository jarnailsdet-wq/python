#Security gate 
idcard=input("have id card : ")
employ=input("Are you employ : ")
check1="yes"
check2="no"

if idcard==check1 and employ==check1:
    print("Access Granted welcome to office")
elif idcard==check1 and employ==check2:
    print("Access denied visitor must registered at the front desk")
else:    
    print("Acces denied no id card found")    
    