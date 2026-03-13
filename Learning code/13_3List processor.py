#list processor
def count_positives(numbers_list):
    counter=0
    for i in range(len(numbers_list)):
        if numbers_list[i]>0:
            return "Postitive"
        elif numbers_list[i]<=0:
            return "Negative"
data=[-2,5,8,-1,10]        
pr=count_positives(data)
print(pr)


     
