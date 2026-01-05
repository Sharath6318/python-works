
nums = [1, 2, 2, 3, 4, 4, 5]



new_set = set(nums) #{1,2,3,4,5}

duplicate_val = set() #{2,4}

for num in nums:

    if(nums.count(num) > 1):

        duplicate_val.add(num)

    slice_array = new_set.symmetric_difference(duplicate_val)

print(f"Elements that appear only once : {slice_array}")

        





    



