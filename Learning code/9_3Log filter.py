#Log filter
urls=["https://sites.com","http://test.org","https://portal.com/login"]
secure_sites=[]
for i in urls:
    print(i)
    if i.startswith ("https") and i.endswith (".com"):
        secure_sites.append(i)
       
print(f"secure_sites : {secure_sites}")
