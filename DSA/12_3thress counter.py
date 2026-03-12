#thres counter
temps=[72,85,90,65,78,92,60]
high_temp=0
for i in range(len(temps)):
    if temps[i]>80:
        print("hightemp")
        high_temp=high_temp+1
print(high_temp)        
