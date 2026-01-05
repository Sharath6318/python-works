# file_path = "_____________TASK_______________/DEC_08_task/Instagram_Analytics.csv"

# fr = open(file_path, encoding="utf-8")

# import csv

# reader = csv.DictReader(fr)

# data = [data for data in reader]

# categorys = [c.get("content_category") for c in data]

# count_of_category = {c : categorys.count(c) for c in categorys}

# max_count = max(count_of_category.values())

# most_common_category = {c for c, n in count_of_category.items() if n == max_count}

# print(most_common_category)

import csv

class Common:

    data : list

    def __init__(self):

        file_path = "_____________TASK_______________/DEC_08_task/Instagram_Analytics.csv"

        fr = open(file_path, encoding="utf-8")

        reader = csv.DictReader(fr)

        data = [data for data in reader]

        self.data = data

    def display_common_category(self):

        categorys = [r.get("content_category") for r in self.data]

        category_wise_count = {c : categorys.count(c) for c in categorys}

        max_count = max(category_wise_count.values())

        common_category = {c for c, n in category_wise_count.items() if n == max_count}

        return common_category


new_instance_01 = Common()

res = new_instance_01.display_common_category()

print(res)




