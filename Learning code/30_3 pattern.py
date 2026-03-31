count=0

for i in range(1,6):
     for j in range(1,6):
         if j>1 and j<5 and i>1 and i<5:
            print("  ",end=" ")  
              
         else :
             count=count+1 
             if count<10:
                 
                 print(f"0{count}",end=" ")   
            # count=count+1 
             else :
                print(count,end=" ")
                
     print("")       
 
 
 