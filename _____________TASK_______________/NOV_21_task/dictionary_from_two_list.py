keys = ["a", "b", "c"] 
values = [1, 2, 3] 

nested_dict = {k : v for k, v in zip(keys, values)}

print(nested_dict)