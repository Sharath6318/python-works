day = int(input("Enter the day between 1 to 7: "))

if day in range (1, 6):

    print("weekDays")

elif day in range (6, 8):

    print("weekEnd")

else:

    print("invalid input")