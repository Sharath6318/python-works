file_path = "PYTHON-WORKS/Error-Handling/process-numbers/numbers.txt"

fr = open(file_path)

lst = []

for line in fr:

    line = line.rstrip("\n")

    try:

        num = int(line)

        lst.append(num)

    except Exception as e:

        continue

print(f"Max num : {max(lst)}")

print(f"Min num : {min(lst)}")

numbers_count = {c : lst.count(c) for c in lst}

max_count = max(numbers_count.values())

max_num = [n for n, c in numbers_count.items() if c == max_count]

print(f"Most Frequent num {max_num}")









    


