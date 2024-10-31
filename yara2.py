vowels= "AEIOUaeiou"
word= input('enter word: ')
word2= " "
for r in word:
    if r not in vowels:
        word2 += r
print("the word without vowels is: ", word2)