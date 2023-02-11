import string
word = "abcd"
word_arr = []
i=1
for letter in word:
    word2 = letter*i
    word_arr.append(word2.capitalize())
    i+=1

print('-'.join(word_arr))
