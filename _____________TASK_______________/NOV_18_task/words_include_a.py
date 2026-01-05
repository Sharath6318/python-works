
fruits = ["apple", "orange", "Apricot", "Avocado", "Banana", "Cantaloupe", "Cherry"]

include_wrd = "a"

word_with_a = []

for word in fruits:

    if(include_wrd in word):

        word_with_a.append(word)


print(word_with_a)