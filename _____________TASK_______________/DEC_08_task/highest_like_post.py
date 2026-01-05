# Find the post with the highest number of likes

import csv

class Reach:

    data : list

    def __init__(self):
        
        file_path = "_____________TASK_______________/DEC_08_task/Instagram_Analytics.csv"

        fr = open(file_path, encoding="utf-8")

        reader = csv.DictReader(fr)

        data = [data for data in reader]

        self.data = data

    def highest_like(self):

        required = {i.get("post_id") : int(i.get("likes")) for i in self.data}

        max_like = max(required.values())

        highest_likes_id = {i for i, r in required.items() if r == max_like}

        print(f"post with the highest number of likes {highest_likes_id} and count {max_like}")

new_instance = Reach()

new_instance.highest_like()



        