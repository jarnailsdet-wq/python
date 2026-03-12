#find the target
bugid=["bug-101","bug-102","bug-103"]
id=input("Enter bug id").lower()
if id in bugid:
    print("Bug found in database")
elif id not in bugid:
    print("Bug not found")    

