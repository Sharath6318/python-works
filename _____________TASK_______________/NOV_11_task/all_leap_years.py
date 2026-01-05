


leap_years = []
def find_leap_year(years):

    for num in range(0, len(years)):

        if(years[num] % 100 == 0 and years[num] % 400 == 0) or (years[num] % 100 != 0 and years[num] % 4 == 0):

            leap_years.append(years[num])

    return leap_years


        
years = [2021, 1999, 1920, 2024, 1852, 1991, 2026, 2000, 2023, 2016, 2009]
print(find_leap_year(years))