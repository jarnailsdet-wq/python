#Browser compatibilty
browser=input("Enter browser name : ")
b1="chrome"
b2="firefox"

if browser==b1:
    print("Best performance")
elif browser==b2:
    print("Standerd performannce")
else:
    print(f"{browser} Browser not supported " )       
