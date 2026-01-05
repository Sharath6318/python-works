file_path = "PYTHON-WORKS\\_____________TASK_______________\\NOV_26_task\\process_move\\movies.txt"

fr = open(file_path)

new_list = []

for line in fr:

    line = line.split("\n")

    new_list.append(line)

for i in range(5):

    res = ''.join(new_list[i])

    print(res)



