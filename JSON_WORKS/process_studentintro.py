from json import load

file_path = "JSON_WORKS\\student_into.json"

fr = open(file_path, encoding="utf-8")

data = load(fr)

photography_intrest = [st.get("name") for st in data if 'Photography' in st.get("interests")]

print(photography_intrest)