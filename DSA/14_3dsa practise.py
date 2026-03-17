#Dsa practise
line=[]
i=0
total=0
total1=0
max=0

total2=0
while(True):   ##### list added 1 100
    i=i+1
    #print(i) 
    line.append(i)
    
    if i==100:
        #print(i)
        break
print(line)
min=len(line)+1

while True:
    Search = input("Enter your search name : ")
    
    match Search:
        case "sum":
            for i in line:        #########Total sum of list
                #print(i)
                total=total+i
            print(f"total of list : {total}")

        case "even":
            for i in range(0,len(line)):                ######### Total of even
                if line[i]%2==0:
                    total1= total1+line[i]
                    #print(total1)
            print(f"Total even numbers : {total1}")        
                
        case "odd":        
            for i in range(0,len(line)):                ######### Total of odd
                if line[i]%2==1:
                    total2= total2+line[i]
                    #print(total1)
            print(f"Total even numbers : {total2}")    
             
        case "maximum":
            for i in range(0,len(line)):  ######### maximum
                if max<=line[i]:
                    max=line[i]
            print(f"maximum number in list : {max}")
            
        case "minimum":
            for i in range(0,len(line)):  ######### minimum
                if min>=line[i]:
                    min=line[i]
                    #print(min)
            print(f"minimum number in list : {min}")


