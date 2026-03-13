#
def check_length(text):
    tr=0
    for i in range(len(text)):
        if i>8:
            return "boolean true"
        elif i<=8:
            return "boolean false"
   
isvalid=check_length("password123")
print(isvalid)


  