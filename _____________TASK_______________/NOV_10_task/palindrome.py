def is_palindrome(str):

    palindrome = True

    reverse_str = str[::-1]

    if(str != reverse_str):

        palindrome = False

    return palindrome
    
print(is_palindrome("abcdcba"))
print(is_palindrome("palindrome"))

