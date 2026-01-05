employee = {"id" :"1234567", "name" : "sharath", "department" : "cs", "location": "thrissur", "salary" : "25000"}

# duplicate val allowed but duplicate key not allow

employee["phone"] = 12343535  # add a key value pair in the DICT

print(employee)

print(employee["location"])  # get employee lacation
print(employee["salary"]) 


if "name" in employee: # check the key precent in the DICT

    print("Exist")

else:

    print("not Exist")