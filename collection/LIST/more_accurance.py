arr = [100,200,300,110,210,200,110,110,100]

freq_val = []

for n in arr:

    if arr.count(n) > 1 and n not in freq_val:

        freq_val.append(n)

print(freq_val)

#withOut using count

# recur_val = []

# for i in range(0, len(arr) - 1):

#     arr.sort()

#     left = arr[i]

#     right = arr[i + 1]

#     if(left - right == 0 and left not in recur_val):

#         recur_val.append(left)

# print(recur_val)














