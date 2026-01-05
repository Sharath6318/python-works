def vowel_count(word):

    count = 0

    vowles = "aeioue"
    for ch in word.casefold():

        if ch in vowles:

            count += 1

    return count

print(vowel_count("hello") ) 
