words = ["hello","hai","hello","is"]

recursive_word = []

for word in words:

    if(words.count(word) > 1 and word not in recursive_word):

        recursive_word.append(word)

print(f"Recursive word are : {recursive_word}")

