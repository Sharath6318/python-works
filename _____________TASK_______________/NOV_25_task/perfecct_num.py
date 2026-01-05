file_path = "C:/Users/HP/OneDrive/Desktop/Project Folder/WEB DEV/Python/PYTHON-WORKS/_____________TASK_______________/NOV_25_task/list_of_numm_txt"

fr = open(file_path, "r")

perfect_num = []

for line in fr:

    line = line.rstrip("\n")

    num = int(line)

    fact_num = set()

    for i in range(1, num): 

        if num % i == 0: 
            
            fact_num.add(i) 

    if sum(fact_num) == num:

        perfect_num.append(num)


print(f"Perfect numbers are : {perfect_num}")


