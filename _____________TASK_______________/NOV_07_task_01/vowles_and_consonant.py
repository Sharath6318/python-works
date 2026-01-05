def vow_and_cons(words):

    vowles_count = 0
    consonant_count = 0     

    vowles = "aeiou"

    for word in words.replace(" ",""):

        if word in vowles:

            vowles_count += 1

        else:

            consonant_count += 1


    print(f"vowles count : {vowles_count}")
    print(f"consonant count : {consonant_count}")

vow_and_cons("pyton programming language")
