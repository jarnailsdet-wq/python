#string reverse
name=input("Enter plaindrome word : ")
revname=""

print("Short cut " , name[::-2])
for i in name:
    revname=i+revname
    print("revname :",revname)
    print("i :",i)
print(revname)
if name==revname:
    print("Word is palindrome")
else:
    print("Not palindrome")    
