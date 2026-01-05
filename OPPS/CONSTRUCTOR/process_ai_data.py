import csv

class Aidataset:

    data = list

    def __init__(self):
        
        file_path = "OPPS/ai_data_process/AI_Impact_on_Jobs_2030.csv"

        fr = open(file_path, encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row for row in reader]

    def total_records(self):

        print(len(self.data))

    def first_recored(self):

        print(self.data[0])


    def job_title(self):

        print([job_t.get("Job_Title") for job_t in self.data])


ai_instance = Aidataset()

# ai_instance.total_records()
# ai_instance.first_recored()
ai_instance.job_title()
