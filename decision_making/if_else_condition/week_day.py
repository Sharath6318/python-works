day = int(input("Enter the day between 1 to 7 :"))

if day <= 5 and day >= 1:

    print("weekday")

elif day <= 7 and day >= 6:

    print("weekend")

else:

    print("invalid input !!")