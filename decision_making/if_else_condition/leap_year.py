year = int(input("Enter the year: "))

# if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):

#     print(year, " is a leep Year")

# else:

#     print(year, "is not a leap year")


if(year % 100 == 0 and year % 400 == 0) or (year % 100 != 100 and year % 4 == 0):

    print(year, "is a leap year")

else:

    print(year, "is not a leap year")
