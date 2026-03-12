#safe Appending
error_codes=[404,500]
new=int(input("Enter new error code : "))
if new not in error_codes:
    print("Not in list")
    error_codes.append(new)
print(error_codes)    