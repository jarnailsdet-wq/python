#nested
retry_count=0
max_retries=3
while retry_count<max_retries:
    print("Attempting to connect to the database")
    status=input("Enter status : ")
    if status=="success":
        print("Connected")
        break
    elif status=="failure":
        retry_count=retry_count+1
        print("Connection failed")
if retry_count==max_retries:
    print("Alert : database offline")

    

    