

def common_item_(data):

    first_set = data[0]
    second_set = data[1]
    third_set = data[2]

    common_items = first_set.intersection(second_set).intersection(third_set)

    print(f"Common item of all set : {common_items}")

data = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
common_item_(data)

