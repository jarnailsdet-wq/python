# List
Fruits=["apple","bnana","grapes","apple","bnana","grapes"]
Fruits.append("kiwe , pine")
Fruits.insert(0,"papaya")
Fruits.extend(["kiwi","papaya"])
#Fruits.extend(Fruits)
#Fruits.clear()
#Updating List
Fruits[0]="dragon"

#Removing list
Fruits.remove("apple")

# POP
Fruits.pop(0)

#delete del
del Fruits[0]

#print(Fruits)
#Looping in list
for item in Fruits:
    print(item)

for i in range(0,10):
    print(i,end="-")