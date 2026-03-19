#Anagram
word1="listen"
word2="silenq"
# for i in word1:
#         #print(i)
#         for j in word2:
#             #print(j)
#             if len(i)==len(j):
                
#                 print("The words have the same length.")
                
if sorted(word1)==sorted(word2):
    print(sorted(word1))
    print(sorted(word2))
    print("The words are anagrams")
else:    
        print("The words are not anagrams.")

