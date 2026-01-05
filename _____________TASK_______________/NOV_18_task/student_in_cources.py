python_students = {"Alice", "Bob", "Charlie"} 
ml_students = {"Bob", "David", "Eve"} 


study_both_languages = python_students.intersection(ml_students)

print(f"who study both Python and ML : {study_both_languages}")

only_study_python_lan = python_students.difference(ml_students)

print(f"who study only Python : {only_study_python_lan}")

either_one = python_students.union(ml_students)

print(f"enrolled in either Python or ML (or both) : {either_one}")