#scenario List and loop
My_browser=["chrome","firefox","safari"]
Valid_ids=[101,102,105,108,110]
My_browser.append("edge")
My_browser.remove("safari")
for i in My_browser:
    print(f"Testing on : {i}")

#Scenario 2
id=int(input("Enter id : "))
if id in Valid_ids:
    print("Id verifies")
else:
    print("Id not recognized")
