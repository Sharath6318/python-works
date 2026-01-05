file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_01_task/spotify_data_clean.csv"

fr = open(file_path, encoding="utf-8", errors="replace")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

new_dict = {}

for row in data:

    artist = row.get("artist_name")

    new_dict[artist] = new_dict.get(artist, 0) + 1


max_track_count = max(new_dict.values())

max_artist = [a for a, s in new_dict.items() if s == max_track_count]

print(f"artist who has the highest number of songs in the dataset : {max_artist}")



    














# new_dict = {}

# songs = [s.get("track_name") for s in data]

# artist_with_songs = {i.get("artist_name") : i.get("track_name") for i in data}


# for s in songs:

#     if s in new_dict:

#         new_dict[s] += 1

#     else:

#         new_dict[s] = 1


# max_song_cou = max(c for s, c in new_dict.items())

# max_song = max(k for k, v in new_dict.items() if v == max_song_cou) #Home

# max_song_artist = [a for a, s in artist_with_songs.items() if s == max_song]

# print(max_song_artist)









