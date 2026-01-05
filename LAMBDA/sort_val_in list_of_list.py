employes_det = [
    ["ram",55000, 3],
    ["keshore", 35000, 1],
    ["akash", 20000, 1],
    ["suriya", 38000, 2],
]

sort_val_by_salary = sorted(employes_det, key=lambda emp : emp[1])

print(sort_val_by_salary)

sort_val_by_exp = sorted(employes_det, key= lambda emp : emp[2])

print(sort_val_by_exp)