#1 Multiple conccept
Bug_reports=[]
pass_list=[]
fail_list=[]
Scores=[45,78,56,34,76,43]
for i in range(1,4):
    Bug=input("Enter bug : ").upper()
    Bug_reports.append(Bug)
print(f"bug report {Bug_reports}")    
   
#Scenario 2 score fiilter

for i in Scores:
    if i>=50:
        pass_list.append(i)
    elif i<=50:
        fail_list.append(i)
    else:
        print("no list")   

print(f"pass report {pass_list}")   
print(f"fail report {fail_list}")   