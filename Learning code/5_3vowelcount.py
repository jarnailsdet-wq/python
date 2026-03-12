#vowel count
text= "python is goodoese"
vowel="aeiou"
vowel_count=0
for i in text:
    #print("i is : ",i)
    # if i=="a" or i=="e" or i=="i" or i=="o" or i=="u": 
    if i in vowel:
        

        vowel_count=vowel_count+1
print("vowel count",vowel_count)
    #else:
       # print("No vowel")