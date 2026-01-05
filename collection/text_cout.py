text = "helloworld"


emty_set = {}

for txt in text:

    if txt in emty_set:

        emty_set[txt] += 1

    else:

        emty_set[txt] = 1


print(emty_set)