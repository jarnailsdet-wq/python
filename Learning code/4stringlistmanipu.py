# String and list manipulation
#Scenario 1
name=input("Enter user name  : ").lower()
if name=="admin":
    print("Welcome admin")
else:
    print("Guest access Granted")

#Scenario 2
Test_Suit=["Login", "Payment","Logout"]
Test_Suit.insert(1,"cart")
Test_Suit.remove("Logout")
print(f"Final List {Test_Suit} ")