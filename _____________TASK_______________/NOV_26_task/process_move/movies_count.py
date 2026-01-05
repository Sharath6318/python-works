file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_26_task/process_move/movies.txt"

fr = open(file_path)

new_list = []

for line in fr:

    line = line.rstrip("\n")

    new_list.append([line])

new_list.remove(new_list[0])

total_move_list = len(new_list)

print(f"Total move list : {total_move_list}")

