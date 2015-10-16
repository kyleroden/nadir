word = list(input("Give a word plz. Then I'll delete the vowels."))

for i in word:
    if 'a' in word:
        word.remove("a")
    elif 'e' in word:
        word.remove('e')
    elif 'i' in word:
        word.remove('i')
    elif 'o' in word:
        word.remove('o')
    elif 'u' in word:
        word.remove('u')    
    elif 'y' in word:
        word.remove('y')
    else:
        break
        
new_word_length = len(word)
counter = 0
word_list = []

while counter < new_word_length:
    word_list += word[counter]
    counter += 1
    continue

print("".join(word_list))
        
##if word[0]:
 ##   print(word[0])
##if word[1]:
 ##   print(word[1])
    