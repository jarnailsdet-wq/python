#Access portal
Correct_username="tester_1"
Correct_password="test@123"
entered_username=input("Enter username : ")
entered_password=input("Enter password : ")
loadtime=float(input("Enter load time : "))

if entered_username==Correct_username and entered_password==Correct_password:
    print("Welcome to the dashboard")
else:
    print("Invalid credentials")

    #Scenario 2

if loadtime<=3.0:
    print("Status : Passed")    
elif loadtime>3.0 and loadtime<5.0:
    print("Status : Slow load")
elif loadtime>=5.0:
    print("Status : failed time out")
else:
    print("time out")    
































