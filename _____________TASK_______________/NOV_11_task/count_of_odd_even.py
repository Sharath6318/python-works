def count_odd_even(arr):
    
    odd_count = 0
    Even_count = 0
    Even_numbers = []
    odd_numbers = []

    for i in range(0, len(arr)):

        if(arr[i] % 2 == 0):

            Even_numbers.append(arr[i])
            Even_count += 1

        else:

            odd_numbers.append(arr[i])
            odd_count += 1

    print(f"odd numbers {odd_count}")
    print(f"Even numbers {Even_count}")
    print(f"Odd count {odd_numbers}")
    print(f"Even count {Even_numbers}")

arr = [1, 5, 7, 9, 12, 15, 16, 19, 20]

count_odd_even(arr)