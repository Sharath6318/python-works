file_path = "C:/Users/HP/OneDrive/Desktop/Project Folder/WEB DEV/Python/PYTHON-WORKS/File-operations/numbers.txt"

odd_num = []
even_num = []

fr = open(file_path, "r")

for line in fr:

    res = int(line.rstrip("/n"))

    if res % 2 == 0 :

        even_num.append(res)

    else:

        odd_num.append(res)

print(odd_num)
print(even_num)
        



