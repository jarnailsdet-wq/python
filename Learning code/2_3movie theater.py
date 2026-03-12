#Movie
Movies_now_playing=["batman","superman","spiderman"]
movie=input("Which u like watch : ")
#age=int(input("Enter your age : "))
if movie in Movies_now_playing:
    age=int(input("Enter your age : "))
    if age>=12:
        print("Ticket confirmed : ")
    elif age<12:
        print("Sory you are too young : ")

else:
    print("Sorry not showing this movies")
