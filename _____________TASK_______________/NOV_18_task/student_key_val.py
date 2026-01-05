student = {"name": "Rahul", "age": 14, "grade": "B"} 


name_of_student = student["name"]

student["school"] = "City High school"

student["grade"] = "A+"

student.pop("age") #remove 

for name_v in student.keys():

    if(name_v in "name"):

        print(f"name of the student : {student[name_v]}")


length_val = len(student)

print(f"length of dict : {length_val}")

for ch in student.keys():

    print(f"keys in the dict : {ch}")

for ch in student.values():

    print(f"values in the dict : {ch}")

for ch in student.items():

    print(f"key values in the dict : {ch}")
