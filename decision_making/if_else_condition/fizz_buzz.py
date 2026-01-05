num = int(input("Enter the number :"))

if num % 15 == 0:

    print("fizzBuzz")

elif num % 5 == 0:

    print("Buzz")

elif num % 3 == 0:

    print("fizz")

else:

    print("invalid input")