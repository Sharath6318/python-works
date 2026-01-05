employees = { 
"E01": {"name": "Arjun", "dept": "HR"}, 
"E02": {"name": "Sara", "dept": "IT"}, 
"E03": {"name": "Manoj", "dept": "Finance"} 
} 

employees["E04"] = {"name": "Lakshmi", "dept": "marketing"} 

# print(employees)

employee_name_id = {k : v.get("name") for k, v in employees.items()}

# print(employee_name_id)

print(len(employees))