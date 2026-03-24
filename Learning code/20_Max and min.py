#max and second max in the list
numbers=[3,5,1,9,2]
max_num=numbers[0]
second_max_num=numbers[0]   

for i in numbers:
    if i>max_num:
        second_max_num=max_num
        max_num=i
    elif i>second_max_num and i!=max_num:
        second_max_num=i

print("Max number:", max_num)
print("Second max number:", second_max_num)