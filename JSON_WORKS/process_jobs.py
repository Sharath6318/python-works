from json import load

file_path = "JSON_WORKS/jobs.json"

fr = open(file_path, encoding="utf-8")

data = load(fr)

python_skills_jobs = [job.get("title") for job in data if "Python" in job.get('skills')]

print(python_skills_jobs)