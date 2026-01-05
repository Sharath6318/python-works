file_path = "C:/Users/HP/OneDrive/Desktop/Project Folder/WEB DEV/Python/PYTHON-WORKS/File-operations/greetings.txt"

fr = open(file_path, "r")

data = {line.rstrip("\n")  for line in fr}  # get all file in string type

print(data)