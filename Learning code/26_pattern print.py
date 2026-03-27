#pattern printing
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print("")  
    
for i in range(1,4):
    for j in range(1,4):
        print(i,end="")
    print("")       
    
for i in range(1,4):
    for j in range(1,4):
        
        print(j,end="")
        
    print("")      
    
for i in range(1,4):
    for j in range(1,4):
        
        print(1,end="")
        
    print("")       


count=0
for i in range(1,4):
    
    for j in range(1,4):
        count=count+1
        print(count,end="")
        
    print("")        