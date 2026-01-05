# intervals = [[1,4], [4,8], [10, 12]]

# merged = []

# merged.append(intervals[0])

# for lst in intervals:

#     if merged[-1][1] >= lst[0]:

#         merged[-1][1] = lst[1]

#     else:

#         merged.append(lst)

# print(merged)

class MergedIntervals:

    def solution(self, intervals):

        merged = []

        merged.append(intervals[0])

        for lst in intervals:

            if merged[-1][1] >= lst[0]:

                merged[-1][1] = lst[1]

            else:

                merged.append(lst)

        return merged

mrg_instance = MergedIntervals()

print(mrg_instance.solution([[1,4], [4,8], [10, 12]]))