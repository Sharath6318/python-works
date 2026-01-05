class Helathanalysis:

    def __init__(self):
        
        file_path = "_____________TASK_______________/DEC_09_task/mental_health_social_media_dataset.csv"

        fr = open(file_path, encoding="utf")

        import csv

        reader = csv.DictReader(fr)

        self.data = [data for data in reader]

    def required(self):

        name_helth = [i.get("person_name") for i in self.data if i.get("mental_state") == "Healthy"]   

        for name in name_helth:

            print(name)


new_instance = Helathanalysis()

new_instance.required()

