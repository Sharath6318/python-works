word = "Python programming is very interesting"

split_wrd = word.split(" ")

updated_wrds = [wrd for wrd in split_wrd if len(wrd) > 5]

print(updated_wrds)