# class ClosestNumberZero:

#     def solution(self, arr):

#         closest_num = arr[0]

#         for num in arr:

#             if abs(num) < abs(closest_num):

#                 closest_num = num

#             if closest_num < 0 and abs(closest_num) in arr:

#                 return abs(closest_num)
#             else:

#                 return closest_num
    
# clst_instance = ClosestNumberZero()

# print(clst_instance.solution([-2, -3, 2, 3, 4]))


# nums = [-2, -3, 2, 3, 4]

# closest_num = min(nums, key=lambda x : abs(x))

# print(closest_num)