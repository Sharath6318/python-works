def is_pangram(word):

    pangram = True

    alphabets = "abcdefghijklmnopqrstuvwxyz"

    for ch in alphabets:

        if(ch not in word):

            pangram = False

            break

    return pangram
            
print(is_pangram("the qucik brown fox jumps over lazy dog"))
print(is_pangram("Hello world"))