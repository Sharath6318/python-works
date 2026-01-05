lst = ["10", "20", "hello", "300", "hai", "4 00"]

new_lst = []

for num in lst:

    try:

        new_lst.append(int(num))

    except Exception as e:

        print(e)

print(new_lst)
