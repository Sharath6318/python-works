file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_01_task/spotify_data_clean.csv"

fr = open(file_path, encoding="utf-8", errors="replace")

count = 0

for line in fr:

    count += 1

print(f"total tracks are available in the dataset : {count}")

