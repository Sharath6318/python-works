file_path = "C:/Users/HP/OneDrive/Desktop/Project Folder/WEB DEV/Python/PYTHON-WORKS/File-operations/numbers.txt"


fr = open(file_path, "r")

reverse = []

for line in fr:

    line = line.rstrip("\n")

    reverse.append(line[::-1])

print(reverse)
  

