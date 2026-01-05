file_path = "PYTHON-WORKS/File-operations/Titanic_process/data_set.csv"

fr = open(file_path, "r")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

name = [name.get("Name") for name in data if name.get("Sex") == "male"] # data name

# for n in name:
     
#      print(n)


# Male_count = len([name.get("Name") for name in data if name.get("Sex") == "male"]) 
# female_count = len([name.get("Name") for name in data if name.get("Sex") == "female"])

# print(f"female count : {female_count}")
# print(f"Male count : {Male_count}")


survived = len([name.get("Survived") for name in data if name.get("Survived") == "1"])

# print(f"survived count : {survived}")


all_class = [c.get("Pclass") for c in data]

class_count = {c : all_class.count(c) for c in all_class}

# print(class_count)

# Youngest and oldest...............

agelist = [int(y.get("Age")) for y in data if y.get("Age").isdigit()]

youngest = min(agelist )
Oldest = max(agelist)

old = {d.get("Name") : d.get("Age") for d in data if d.get("Age") == str(Oldest)}
young = {d.get("Name") : d.get("Age") for d in data if d.get("Age") == str(youngest)}

# print(f"oldest passenger {old}")
# print(f"Youngest passenger {young}")

# first 10 data 

required_data = data[:10]

first_ten = [data.get("Name") for data in required_data]

# print(first_ten)

# count of boarding stations

all_passengers_bording_station = [b.get("Embarked") for b in data if len(b.get("Embarked")) > 0]

bc = {p : all_passengers_bording_station.count(p) for p in all_passengers_bording_station}

# print(bc)


children  = [info for info in data if info.get("Age").isdigit() and int(info.get("Age")) < 10]

below_age_10_children_cou = len(children)

# print(f"Age below 10 : {below_age_10_children_cou}")

survived_children = [p for p in children if p.get("Survived") == "1"]

# print(f"survived_children_count : {len(survived_children)}")

# survival rate....................


survived_pass = [i for i in data if i.get("Survived") == "1"]

survived_pass_cou = len(survived_pass)

# print(survival)
total_survival_per = (survived_pass_cou /len(data)) * 100

# print(total_survival_per)

men_survival = [i for i in data if i.get("Survived") == "1" and i.get("Sex") == "male"]
women_survival = [i for i in data if i.get("Survived") == "1" and i.get("Sex") == "female"]

cou_male_survial = len(men_survival)
cou_female_survial = len(women_survival)

men = [m for m in data if m.get("Sex") == "male"]
women= [m for m in data if m.get("Sex") == "female"]

men_cou = len(men)
women_cou = len(women)

survival_men_per = round((cou_male_survial/men_cou) * 100, 2)
survival_women_per = round((cou_female_survial/women_cou) * 100, 2)

# print(survival_men_per)
# print(survival_women_per)

all_class = [info.get("Pclass") for info in data]
survival_all_class = [info.get("Pclass") for info in data if info.get("Survived") == "1"]
dead_of_all_class = [info.get("Pclass") for info in data if info.get("Survived") == "0"]

class_wise_cou = {c : all_class.count(c) for c in all_class}
class_wise_sur_cou = {c : survival_all_class.count(c) for c in survival_all_class}
class_wise_dead_cou = {c : dead_of_all_class.count(c) for c in dead_of_all_class}

for k, v in class_wise_cou.items():

    s_p = class_wise_sur_cou.get(k)

    rate = round((s_p/ v) * 100, 2)

    print(k,"class", rate)

# print(f"all pasenger count class wise : {class_wise_cou}")
# print(f"survived count in class wise {class_wise_sur_cou}")
# print(f"Non survival count in class wise {class_wise_dead_cou}")

# survival = [s.get("Survived") for s in data]

# print(survival)






