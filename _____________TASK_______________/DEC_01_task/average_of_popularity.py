file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_01_task/spotify_data_clean.csv"

fr = open(file_path, encoding="utf-8", errors="replace")

import csv

reader = csv.DictReader(fr)



data = [data for data in reader]

true_explicity_track_popularity = [p.get("track_popularity") for p in data if p.get("explicit") == "TRUE"]
false_explicity_track_popularity = [p.get("track_popularity") for p in data if p.get("explicit") == "FALSE"]

sum_val_T = sum([int(num) for num in true_explicity_track_popularity])
len_val_T = len(true_explicity_track_popularity)

sum_val_F = sum([int(num) for num in false_explicity_track_popularity])
len_val_F = len(false_explicity_track_popularity)

average_of_true_explicity = round((sum_val_T / len_val_T), 2)
average_of_false_explicity = round((sum_val_F / len_val_F), 2)

print(average_of_true_explicity)
print(average_of_false_explicity)



