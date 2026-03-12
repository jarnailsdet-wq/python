# custom count
word= "automationaa"
target_letter= "a"
occurrence=0

for i in word:
    if i==target_letter:
        occurrence=occurrence+1
    final1="the letter {} appears {} times".format(target_letter,occurrence)
print(final1)

