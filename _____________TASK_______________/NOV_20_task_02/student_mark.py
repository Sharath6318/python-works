student_mark = {"Aju": 92, "Binu": 76, "Chandru": 64}

new_dict = {name : ("A" if (mark > 90) else "B" if (mark > 70 ) else "C" if (mark > 60) else "D") for name, mark in student_mark.items()}

print(new_dict)
