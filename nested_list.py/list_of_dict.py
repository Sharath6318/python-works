vehicles = [
    {"name": "Swift", "brand": "Maruti Suzuki", "price": 650000, "model": 2021, "color": "White", "fuel_type": "Petrol"},
    {"name": "Baleno", "brand": "Maruti Suzuki", "price": 820000, "model": 2022, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Creta", "brand": "Hyundai", "price": 1500000, "model": 2023, "color": "Black", "fuel_type": "Diesel"},
    {"name": "i20", "brand": "Hyundai", "price": 950000, "model": 2021, "color": "Red", "fuel_type": "Petrol"},
    {"name": "Seltos", "brand": "Kia", "price": 1600000, "model": 2023, "color": "Silver", "fuel_type": "Diesel"},
    {"name": "Sonet", "brand": "Kia", "price": 1200000, "model": 2022, "color": "Grey", "fuel_type": "Petrol"},
    {"name": "Harrier", "brand": "Tata", "price": 1900000, "model": 2023, "color": "White", "fuel_type": "Diesel"},
    {"name": "Nexon", "brand": "Tata", "price": 1200000, "model": 2022, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Punch", "brand": "Tata", "price": 800000, "model": 2023, "color": "Green", "fuel_type": "Petrol"},
    {"name": "XUV700", "brand": "Mahindra", "price": 2200000, "model": 2023, "color": "Black", "fuel_type": "Diesel"},
    {"name": "Thar", "brand": "Mahindra", "price": 1700000, "model": 2022, "color": "Red", "fuel_type": "Petrol"},
    {"name": "Scorpio N", "brand": "Mahindra", "price": 2000000, "model": 2023, "color": "White", "fuel_type": "Diesel"},
    {"name": "City", "brand": "Honda", "price": 1500000, "model": 2021, "color": "Silver", "fuel_type": "Petrol"},
    {"name": "Amaze", "brand": "Honda", "price": 900000, "model": 2022, "color": "Grey", "fuel_type": "Petrol"},
    {"name": "Kiger", "brand": "Renault", "price": 800000, "model": 2021, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Duster", "brand": "Renault", "price": 1300000, "model": 2020, "color": "Brown", "fuel_type": "Diesel"},
    {"name": "EcoSport", "brand": "Ford", "price": 1100000, "model": 2021, "color": "White", "fuel_type": "Petrol"},
    {"name": "Endeavour", "brand": "Ford", "price": 3600000, "model": 2020, "color": "Black", "fuel_type": "Diesel"},
    {"name": "Altroz", "brand": "Tata", "price": 950000, "model": 2022, "color": "Golden", "fuel_type": "Petrol"},
    {"name": "Venue", "brand": "Hyundai", "price": 1300000, "model": 2023, "color": "Red", "fuel_type": "Petrol"}
]


vechile_name = [v.get("name") for v in vehicles]
vechile_brand = {v.get("brand") for v in vehicles}
vechile_prices = {v.get("price") for v in vehicles}
color_red_vechile = [v.get("name") for v in vehicles if v.get("color")  == "Red"]
model_2022_vechile_names = {v.get("name") for v in vehicles if v.get("model") == 2022}
diesel_vechile_names = {v.get("name") for v in vehicles if v.get("fuel_type") == "Diesel"}
below_10_lack_vechiles = [v.get("name") for v in vehicles if v.get("price") < 1000000]
tata_vech_model_2022 = [v.get("name") for v in vehicles if v.get("brand") == "Tata" and v.get("model") == 2022]
maruthi_suzuki_vehiles_price = [v.get("price") for v in vehicles if v.get("brand") == "Maruti Suzuki"] 
hundayi_vechiles_great_fivelack = {v.get("name") for v in vehicles if v.get("price") > 500000 and v.get("brand") == "Hyundai"}
vechile_at_2022_to_2024 = {v.get("name") for v in vehicles if v.get("model") <= 2024 and v.get("model") >= 2022}


# print(f"Vechile Names : {vechile_name}")
# print(f"Vechile brands : {vechile_brand}")
# print(f"Vechile prices : {vechile_prices}")
# print(f"Vechile in red color : {color_red_vechile}")
# print(f"Vechile in 2022 : {model_2022_vechile_names}")
# print(f"Vechile run in diesel  : {diesel_vechile_names}")
# print(f"Vechile below 10 lack  : {below_10_lack_vechiles}")
# print(f"tata launch vechile in 2022  : {tata_vech_model_2022}")
# print(f"prices of maruthi suzuki vehicles  : {maruthi_suzuki_vehiles_price}")
# print(f"hundayi vehicle names avaiale at grater 5lac  : {hundayi_vechiles_great_fivelack}")
# print(f"vehicle names whose model in range of 2022 - 2024 : {vechile_at_2022_to_2024}")











