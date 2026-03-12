#automated email(.format)
Dev_name="Alex"
Module="Payment gateway"
Error_code="502"
Message="Hello {}, the {} Failed with code {}".format(Dev_name,Module,Error_code)
print(Message)

#Message2="Hello {} {} Welcome to cafetreria Please have your coffe on your table 67"
Name=input("Add your name : ")
block=input("Enter your block number : ")
time=int(input("Enter your time : "))

if time>=9 and time<12:
    Message2="Hello {} Good morning Welcome to cafetreria of block number {} Please have your coffe on your table 67".format(Name,block)
    print(Message2)
elif time>=12 and time<18:    
   Message3="Hello {} Good Evening Welcome to cafetreria of block number {} Please have your Tea on your table 77".format(Name,block)
   print(Message3) 
else:
    print("Please go to admin counter")   





