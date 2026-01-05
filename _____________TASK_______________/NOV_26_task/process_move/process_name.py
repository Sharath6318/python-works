file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_26_task/process_move/movies.txt"

fr = open(file_path)

row = fr.readline()

for line in row:

    line = row.rstrip("\n")

    word = line.split(",")

for w in word:

    print(w)



    


    