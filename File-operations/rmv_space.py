file_path = "C:/Users/HP/OneDrive/Desktop/Project Folder/WEB DEV/Python/PYTHON-WORKS/File-operations/words.txt"

fr= open(file_path, "r")

res = []

for line in fr:

    line = line.rstrip("\n")

    word = line.replace(" ", "")

    res.append(word)

print(res)
