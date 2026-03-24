#find second min number
numbers=[3,4,1,9,6,2]
min=numbers[0]
second_min=numbers[0]

for i in numbers:
    if i<second_min:
        second_min=min
        min=i
    elif i<second_min and i!=min:
            second_min=i
            
print("Min number:", min)
print("Second min number:", second_min)         