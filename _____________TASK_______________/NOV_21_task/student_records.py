students = { 
"101": {"name": "Rahul", "age": 14, "grade": "B"}, 
"102": {"name": "Anita", "age": 15, "grade": "A"} 
} 


res = {k : v.get("name") for k, v in students.items()}

# print(res)

students["103"] = {"name": "Vikram", "age": 16, "grade": "B+" }

print(students)