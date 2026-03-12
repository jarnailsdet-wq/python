#test error
# user_age= int(input("Enter your age:"))
# if user_age<18:
#     print("underage user")
# else:
#     print("Valid User")

# retries=0 
# # retries=int(input("Enter number of retries : "))
# while retries<3:
#     #retries=int(input("Enter number of retries : "))
#     print(retries)
#     retries=retries+1
#     print(f"pinging server.... Attempt {retries}")
#     if retries==3:
#         print("Server down.")

# api_status=404
# match api_status:
#     case 200:
#         print("OK")
#     case 500:
#         print("Internal Server Error")
#     case  _:
#         print("Unknown error")

# raw_log = " e-r-r-o-r- -4-0-4"
# clean=raw_log.replace("-","")
# clean=clean.strip()
# clean=clean.upper()
# print(f"Expected output : {clean}")


tickets = ["BUG-101", "FEATURE-99", "BUG-102", "TASK-4", "BUG-103"]
bug_tickets = []
for i in tickets:
    print("-"*15+"loop"+"-"*15)
    print(i)
    if i.startswith("BUG"): 
        bug_tickets.append(i)
        print(bug_tickets)


print("-"*15+"OUTPUT"+"-"*15)
print(f"Total bugs : {len(bug_tickets)}")        