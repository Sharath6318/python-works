class ClosestNumberZero:

    def solution(self, arr):

        closest_num = arr[0]

        for num in arr:

            if abs(num) < abs(closest_num):

                closest_num = num

            if closest_num < 0 and abs(closest_num) in arr:

                return abs(closest_num)
            else:

                return closest_num
    
clst_instance = ClosestNumberZero()

print(clst_instance.solution([-2, -3, 2, 3, 4]))