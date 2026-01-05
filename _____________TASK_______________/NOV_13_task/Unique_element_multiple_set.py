a = {1, 2}
b = {2, 3}
c = {3, 4}
d = {4, 5}

unique_values = a.symmetric_difference(b).symmetric_difference(c).symmetric_difference(d)
      
print(f"Unique values are : {unique_values}")
