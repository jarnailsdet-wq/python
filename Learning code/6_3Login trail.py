#Login trail
trail=5
while(trail>0):
    value=input("Enter password : ")
    if value=="A":
        print("logic success")
        break
    else :
        trail=trail-1
        
        print(f"try agian trail left {trail}")
