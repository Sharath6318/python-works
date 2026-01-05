file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_26_task/process_move/movies.txt"

fr = open(file_path)

user_input = input("Enter the year : ") 

split_by_line = []

for line in fr:

    line = line.rstrip("\n")

    split_by_line.append(line.split(","))


for l in split_by_line:

    if user_input in l :

        print(l)
    
