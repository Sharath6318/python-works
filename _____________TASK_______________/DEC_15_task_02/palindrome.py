def is_palindrome(s):
    if s == "":
        return True
    if len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


print(is_palindrome("madam"))  
print(is_palindrome("name"))   
