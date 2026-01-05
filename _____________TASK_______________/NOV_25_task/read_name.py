file_path = "C:/Users/HP/OneDrive/Desktop/Project Folder/WEB DEV/Python/PYTHON-WORKS/_____________TASK_______________/NOV_25_task/names.txt"

first_char = []

last_char = []

fr = open(file_path, "r")

for line in fr:

    line = line.rstrip("\n")

    first_char.append(line[0])

    last_char.append(line[len(line) -1])

print(f"First char : {first_char}")
print(f"last char : {last_char}")



    