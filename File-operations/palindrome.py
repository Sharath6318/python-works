file_path = "C:/Users/HP/OneDrive/Desktop/Project Folder/WEB DEV/Python/PYTHON-WORKS/File-operations/words.txt"

fr = open(file_path, "r")

pali = []

for line in fr:

    line = line.rstrip("\n").replace(" ", "")

    if line == line[::-1]:

        pali.append(line)

print(pali)