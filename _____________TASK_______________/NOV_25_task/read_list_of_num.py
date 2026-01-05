file_path = "C:/Users/HP/OneDrive/Desktop/Project Folder/WEB DEV/Python/PYTHON-WORKS/_____________TASK_______________/NOV_25_task/list_of_num.txt"

fr = open(file_path, "r")

odd_num = []
even_num = []

for line in fr:

    line = line.rstrip("\n")

    int_val = int(line)

    if int_val % 2 == 0:

        odd_num.append(int_val)

    else:

        even_num.append(int_val)

print(f"Even numbers : {odd_num}")
print(f"Odd numbers : {even_num}")

    