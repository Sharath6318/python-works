mobile_brands = {"Samsung", "Apple", "OnePlus", "Vivo"} 
budget_brands = {"Vivo", "Realme", "OnePlus"} 

not_budget_friendly = mobile_brands.difference(budget_brands)

print(f"not budget friendly mobile phones : {not_budget_friendly}")

