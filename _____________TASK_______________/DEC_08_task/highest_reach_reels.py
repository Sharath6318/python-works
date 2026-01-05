# highest reach reels id and reach count

import csv

class Reach:

    data : list

    def __init__(self):
        
        file_path = "_____________TASK_______________/DEC_08_task/Instagram_Analytics.csv"

        fr = open(file_path, encoding="utf-8")

        reader = csv.DictReader(fr)

        data = [data for data in reader]

        self.data = data

    def highest_reach(self):

        required = {i.get("post_id") : int(i.get("reach")) for i in self.data if i.get("media_type") == "Reel"}

        high_reach = max(required.values())

        highest_reach_reel_id = {i for i, r in required.items() if r == high_reach}

        print(f"Highest reach reels id {highest_reach_reel_id} reach count {high_reach}")

new_instance = Reach()

new_instance.highest_reach()



        