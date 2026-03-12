# Smart Browser Check
allowed=["chrome","safari","edge"]
browser=input("Enter your browser : ").lower()
if browser in allowed:
    print("Test started")
else:
   print("Invalid browser")    
