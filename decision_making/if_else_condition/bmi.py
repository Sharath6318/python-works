weight_in_kg = int(input("Enter the weight :"))

height_in_cm = int(input("Enter the height :"))

height_in_meter = height_in_cm/100

BMI = round(weight_in_kg/(height_in_meter**2),0)



print(BMI)

if BMI < 20:

    print("under Weight")

elif BMI < 25 :
    
    print("normal weight")

elif BMI < 30 :

    print("overWeight")

elif BMI >= 30:

    print("obese")


