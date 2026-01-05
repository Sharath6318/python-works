file_path = "PYTHON-WORKS\\File-operations\\word_count\\story.txt"

fr = open(file_path, "r")

emty_dict = {}

for line in fr:

    line = line.rstrip("\n").split(" ")

    for word in line:

        word = word.rstrip(",")

        if word in emty_dict:

            emty_dict[word] += 1

        else:

            emty_dict[word] = 1

max_count = max(emty_dict.values())

max_value = {k : v for k, v in emty_dict.items() if v == max_count and k.isalpha()}

print(max_value)


