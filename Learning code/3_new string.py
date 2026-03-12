# new string
v1="heri"
v2='   abhi   '
v3="""
hello i am learing python
hello i am learning sql
"""

v4='''
hello i am learing python
hello i am learning sql

'''
# print(v1)
# print(v2)
# print(v3)
# print(v4)

# print(v1[1])
# print(v1[1:3])  #"heri" its print : er
# print(v4[1::6])  #"hello heri 123" its print : er "it lerave 6 charecter"

for i in v1:
    print(i)

v5="H"+v1[1:] #
print(v5)

print(len(v1))
print(v2.strip())
print(v2)
print(v3.replace("i","we"))
v3 = v3.replace("i","he")
print(v3)

print("-"*20)

print(v1+v2) # concetination

s="my name is {} and i am {} old".format("heri",22)
print(s)


print("pythod" in v3 )
