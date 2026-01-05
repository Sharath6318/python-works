# hash tag count 0

import csv

class Reach:

    data : list

    def __init__(self):
        
        file_path = "_____________TASK_______________/DEC_08_task/Instagram_Analytics.csv"

        fr = open(file_path, encoding="utf-8")

        reader = csv.DictReader(fr)

        data = [data for data in reader]

        self.data = data

    def hash_tag_count_0(self):

        count = 0

        for i in self.data:

            if int(i.get("hashtags_count")) == 0:

                count += 1

        print(f"count of media type have 0 hash_tags {count}")

new_instance = Reach()

new_instance.hash_tag_count_0()





        