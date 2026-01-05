file_path = "PYTHON-WORKS/Error-Handling/process_nums/nums.txt"

fr = open(file_path, encoding="utf-8")

all_nums = []

for line in fr:

    line = line.rstrip("\n")

    all_nums.append(line)

print(all_nums)

even_nums = []

for ele in all_nums:

    try:

        int_val = int(ele)

        if int_val % 2 == 0:

            even_nums.append(ele)

    except:

        continue

print(f"Even numbers : {even_nums}")

count_dict = {num : even_nums.count(num) for num in even_nums}

print(f"Count of numbes {count_dict}")

max_count = max(count_dict.values())

for n , c in count_dict.items():

    if c == max_count:

        print(f"Most occurance num : {n}")