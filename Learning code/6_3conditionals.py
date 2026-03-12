#while
num=5
for i in range(1,6):
    
    if i>=3:
        pass
    print(i,end=" ,")
        
print()
while(num>0):
    print(num)
    
num =5 

#match
match num:
    case 1:
        print(1)
    case 4|5:
        print(4,5)    

#
age=16
s="Adult" if age>=18 else"miner"
print(s)
