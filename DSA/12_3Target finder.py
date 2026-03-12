#target finder
numbers=[14,25,33,41,58]
target=33
for i in range(len(numbers)):
    if numbers[i]==target:
        print(numbers[i])
        print(f"target found at index:{i}")
        break
    
