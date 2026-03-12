#subtractting search
logs=["pas: Login","  Fail : Checkout  ","Pass: Search","pass: Fail"]
Failed_test=[]
Failed_test2=[]
pass_search=[]
nin=[]
count=0
for i in logs:
    count=count+1
    
    print("-"*15+"loop "+str(count)+"-"*15)
    print(f"vallue of i : {i}")
    i=i.strip()
    if "Fail" in i:                              # first if
        print("Enter first if")
        Failed_test.append(i)
        print("failed test 1 : " ,Failed_test)   
        print("failed test 2 : " ,Failed_test2)
        print("pass_search : " ,pass_search)
        print("nin : " ,nin)
    if i.startswith ("Fail"):                   #second if
        print("Enter second if")
        Failed_test2.append(i)
        print("failed test 1 : " ,Failed_test)   
        print("failed test 2 : " ,Failed_test2)
        print("pass_search : " ,pass_search)
        print("nin : " ,nin)
    if not i.endswith("Search"):                    #third if
        print("Enter third if")
        pass_search.append(i)
        print("failed test 1 : " ,Failed_test)   
        print("failed test 2 : " ,Failed_test2)
        print("pass_search : " ,pass_search)
        print("nin : " ,nin)        
    if "Fail" not in i:                             #fourth if
        print("Enter fourth if")
        nin.append(i)
        print("failed test 1 : " ,Failed_test)   
        print("failed test 2 : " ,Failed_test2)
        print("pass_search : " ,pass_search)
        print("nin : " ,nin)        


print("failed test 1 : " ,Failed_test)   
print("failed test 2 : " ,Failed_test2)
print("pass_search : " ,pass_search)
print("nin : " ,nin)
