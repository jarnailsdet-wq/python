#Checking box
Active_user=["admin","tester_1","dev_05"]
name=input("Enter user name : ")
if name in Active_user:
    print("Access granted")
elif name not in Active_user:
    print("User not found")
