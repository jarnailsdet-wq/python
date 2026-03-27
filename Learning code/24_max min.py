#max min

item=[34,66,43,11,22,77]
max=0
min=100
for i in item:
    
    if i>max:
        max=i

    if i<min:
       min=i 
    
print(f"maximum value {max}")    
print(f"minimum value {min}")