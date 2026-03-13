#list processor
def count_positives(numbers_list):
    counter=0
    for i in range(len(count_positives)):
        if count_positives[i]>0:
            return "Postitive"
        elif count_positives[i]<=0:
            return "Negative"
data=[-2,5,8,-1,10]        
pr=count_positives(data)
print(pr)


     
