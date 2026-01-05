students = { 
"101": {"name": "Rahul", "age": 14, "grade": "B"}, 
"102": {"name": "Anita", "age": 15, "grade": "A"} ,
"103": {"name": "vikram", "age": 16, "grade": "C"} 
} 

required_data = {k : v.get("name") for k, v in students.items()}

print(required_data)