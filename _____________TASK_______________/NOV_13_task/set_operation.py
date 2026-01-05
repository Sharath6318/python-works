A = {1,2,3,4,5}
B = {4,5,6,7,8}

common_item = A.intersection(B)
print(f"Common items : {common_item}")

difference = A.difference(B)
print(f"The item in A but not in B : {difference}")

symmetirc_difference = A.symmetric_difference(B)
print(f"Symmetric Difference of A and B : {symmetirc_difference}")
