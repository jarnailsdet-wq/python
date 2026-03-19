#Move zero to the end
data=[0,1,0,3,12]
clean_data=[]
zero=[]
zerocount=0

for i in data:
    if i!=0:
       clean_data.append(i)
      # print(clean_data) 
#for i in data:
    if i==0:
       
        zero.append(i)
        zerocount=zerocount+1
        #print(zero)
        
for i in zero:
    clean_data.append(i)  
    
print(clean_data)          
        
     