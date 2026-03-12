#code review
#section A
browser_list=["chrome","safari","edge"]
user_choice=input("Enter your browser : ")
if user_choice in browser_list:
    print("browser is supported")
else:
    print("browser not found")
    
    #section B
attempts = int(input("how many retires? ")) 
for i in range(attempts):
    print("Testing...")