text = "Python is easy and Python is powerful"

u_txt = text.replace(" ", "").casefold()


unique_words = set()

for wrd in u_txt:

    unique_words.add(wrd)

print(unique_words)











