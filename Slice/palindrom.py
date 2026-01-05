
def is_palindrome(word_1):

    word = word_1.casefold()

    return (word == word[::-1])


print(is_palindrome("Radar"))

#string:

# anagram
# panagram
# palindrome
# kangraooword
# longest sequence palindrome in given string
# merge string