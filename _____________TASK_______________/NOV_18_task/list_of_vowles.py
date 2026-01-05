
word = "programming"

vowles = "aeiou"

vowles_words = []

for ch in word:

    if(ch in vowles):

        vowles_words.append(ch)

print(f"Vowles words in {word} : {vowles_words} ")