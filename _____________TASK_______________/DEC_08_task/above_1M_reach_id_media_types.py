# above 1M reach user id,  content type

import csv

class Reach:

    data : list

    def __init__(self):
        
        file_path = "_____________TASK_______________/DEC_08_task/Instagram_Analytics.csv"

        fr = open(file_path, encoding="utf-8")

        reader = csv.DictReader(fr)

        data = [data for data in reader]

        self.data = data

    def above_1M_reach(self):

        required = {i.get("post_id") : i.get("media_type") for i in self.data if int(i.get("reach")) > 1000000}

        print(required)

new_instance = Reach()

new_instance.above_1M_reach()





        