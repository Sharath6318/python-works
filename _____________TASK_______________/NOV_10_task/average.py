def average_list(lis):

    count_lis = len(lis)

    sum = 0

    for i in range(0, len(lis)):

        sum += lis[i] / count_lis

    return round(sum)

list_val = [10, 20, 30, 40, 50]

print(average_list(list_val))
