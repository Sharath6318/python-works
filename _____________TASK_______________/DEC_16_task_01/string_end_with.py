str_val = "Python is an interpreted high-level programming language"

word = "moon"

split_str_val = str_val.split(" ")

def isendwith(word):

    if split_str_val[-1] == "moon":

        return True
    
    else:

        return False
    
print(isendwith(word))



