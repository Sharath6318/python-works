years=[2005,2004,2008,2010,2024,2028,2024,2005]


leap_year = [year for year in years if(year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)]


print(leap_year)