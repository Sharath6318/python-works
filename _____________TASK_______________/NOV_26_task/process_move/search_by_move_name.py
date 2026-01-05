file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_26_task/process_move/movies.txt"

fr = open(file_path)

fr.readline()

user_input = input("Enter the keyword : ")

for line in fr:

    line = line.rstrip("\n")

    res = line.split(",")

    if user_input in res:

        print(res)



