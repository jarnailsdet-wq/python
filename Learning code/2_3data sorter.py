# data sorter
numbers=[12,55,8,100,33,7,90]
high=[]
low=[]
for i in numbers:
    if i>=50:
        high.append(i)
    elif i<=50:
        low.append(i)
    else:
        print("no list")   

print(f"high number {high}")   
print(f"low number {low}") 