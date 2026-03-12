#Batchrunner
code=[200,404,500,200]
countpasses=0
bugerror=0
#value=int(input("Enter the code : "))
for i in code: #code[0]
    if i==200:
        print(f"test case pass : status {i}")
        countpasses=countpasses+1
    else:
        print(f"Test case fail : Status {i}")
        bugerror=bugerror+1
    print(f"bugs : {bugerror} \n Passes : {countpasses}")       

