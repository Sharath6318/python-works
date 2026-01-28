file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/student_data.csv"


fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

MCQ_XOBIN_PYTHON = [float(info.get("MCQ_XOBIN")) for info in data if len(info.get("MCQ_XOBIN")) > 1 and info.get("BATCH ") == "Python"]

MCQ_XOBIN_DATA_SCIENCE = [float(info.get("MCQ_XOBIN")) for info in data if len(info.get("MCQ_XOBIN")) > 1 and info.get("BATCH ") == "Data Science"]

OVERALL = [float(info.get("MCQ_XOBIN")) for info in data if len(info.get("MCQ_XOBIN")) > 1]

Average_MCQ_XOBIN_python = round((sum(MCQ_XOBIN_PYTHON) / len(MCQ_XOBIN_PYTHON)), 2)
Average_MCQ_XOBIN_Datascience = round((sum(MCQ_XOBIN_DATA_SCIENCE) / len(MCQ_XOBIN_DATA_SCIENCE)), 2)
Average_MCQ_XOBIN_Overall = round((sum(OVERALL) / len(OVERALL)), 2)

print(f"Average MCQ_XOBIN for Python batch {Average_MCQ_XOBIN_python}")
print(f"Average MCQ_XOBIN for Data Science batch {Average_MCQ_XOBIN_Datascience}")
print(f"Average OVERALL for both batches {Average_MCQ_XOBIN_Overall}")

