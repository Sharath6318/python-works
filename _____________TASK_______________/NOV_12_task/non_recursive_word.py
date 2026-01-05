words = ["hello","hai","hello","is"]

non_recursive_word = []

for word in words:

    if(words.count(word) <= 1 and word not in non_recursive_word):

        non_recursive_word.append(word)

print(non_recursive_word)