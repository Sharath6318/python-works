weight_kg = int(input("Enter the weight :"))
height_cm = int(input("Enter the weight in cm :"))

def bmi(weight_in_kg, height_in_cm):

    height_in_meter = height_in_cm/100

    BMI = round(weight_in_kg/(height_in_meter ** 2))

    return BMI

print(bmi(weight_kg, height_cm))
