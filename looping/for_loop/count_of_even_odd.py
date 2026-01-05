num = int(input("Enter the number :"))

odd_count = 0
even_count = 0

for i in range(1, num + 1):

    if(i % 2 == 0):

        odd_count += 1

    else:

        even_count += 1

print(f"Odd count {odd_count}")

print(f"Even count {even_count}")


# eucledian algoritham for lcm