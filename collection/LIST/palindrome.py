


def palindrome_wrods(words):

    palindrome_w= []

    for word in words:

        if(word == word[::-1]):

            palindrome_w.append(word)

    return palindrome_w


words = ["cat", "act", "dam", "mad", "malayalam", "madam"]

print(palindrome_wrods(words))

