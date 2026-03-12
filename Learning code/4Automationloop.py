#Automation Loop
load_Times=[1.2,2.5,3.8,0.9,4.1]
for time in load_Times:
    if time<=3.0:
        print(f"fail Load time {time} is too slow")
    else:
        print(f"pass : Load time {time} is acceptable")

