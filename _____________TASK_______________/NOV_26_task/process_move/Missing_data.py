file_path = "PYTHON-WORKS\\_____________TASK_______________\\NOV_26_task\\process_move\\movies.txt"


fr = open(file_path)

header = fr.readline()
columns = len(header.split(","))

for line in fr:
        
    line = line.rstrip("\n")

    row = line.split(" ")

    if len(row) < columns:

        print(row)
