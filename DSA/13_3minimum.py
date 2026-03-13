#minimum find in dsa
times=[12.5,9.2,14.1,8.8,10.5]
minmum=times[0]
for i in range(len(times)):
    if times[i]<minmum:
        minmum=times[i]
print(minmum)    