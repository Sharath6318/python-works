year = int(input("Enter the year :"))

def leap_year(year):

    return True if(year % 100 == 0 and year % 400 == 0) or (year % 100 != 100 and year % 4 == 0) else False

print(leap_year(year))