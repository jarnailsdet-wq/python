#String vs variable
environment="Production"
test_id=99
#print(environment+test_id)
print(environment+str(test_id))
#test_id=str(test_id)
print(type(test_id))
print("Runing test " +str(test_id)+ " in  the "+environment+ " environment")
v1=("Runing test {} in the {} environment".format(str(test_id),environment))
print(f"Runing Test {str(test_id)} in the {environment} envirnoment")
print(v1)