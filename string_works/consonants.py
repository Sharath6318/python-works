def consonants(word):

    count = 0
    consonants_val = "aeiou"

    for ch in word.casefold():

        if ch not in consonants_val and ch.isalpha():

            count += 1

    return count

print(consonants("hello"))
print(consonants("world123"))