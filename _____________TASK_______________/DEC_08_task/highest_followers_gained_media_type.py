# Top three post with highest followers gained...................

import csv

class Reach:

    data : list

    def __init__(self):
        
        file_path = "_____________TASK_______________/DEC_08_task/Instagram_Analytics.csv"

        fr = open(file_path, encoding="utf-8")

        reader = csv.DictReader(fr)

        data = [data for data in reader]

        self.data = data

    def most_folowers_gained(self):

        sort_val = sorted(self.data, key=lambda d : int(d.get("followers_gained")), reverse=True)

        print(sort_val[:3])


new_instance = Reach()

new_instance.most_folowers_gained()





        