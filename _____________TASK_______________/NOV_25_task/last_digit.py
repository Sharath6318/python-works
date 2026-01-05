file_path = "C:/Users/HP/OneDrive/Desktop/Project Folder/WEB DEV/Python/PYTHON-WORKS/_____________TASK_______________/NOV_25_task/several_num.txt"

fr = open(file_path, "r")

result = []


for line in fr:

    line = line.rstrip("\n")

    last_digit = line[len(line) - 1]

    result.append(last_digit)


print(f"Last digit of the numbers : {result}")