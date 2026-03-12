#

arr=[3,5,7,5,3,1,4,6,8,]
target=8
i=0
ent=0
count=0
sum=0
ent=int(input("Enter your input"))
for i in range(0,len(arr)):
    #print(i)
    if ent==arr[i]:
        #print("Find")
        print(f"Found at index : {i}")
        break
    else:    
        print("Not found")




        
        
