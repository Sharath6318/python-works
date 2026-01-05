
            # Simple Calculator


num1 = int(input("Enter the num1 value :"))

num2 = int(input("Enter the num2 value :"))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
exponentitation = num1 ** num2

print(num1,"and", num2, "addition value :", addition, 
      "subtraction value :",subtraction,
      "multiplication value :",multiplication, 
      "division value :",division)

print(f"Floor division value {floor_division}")

print(f"Modulus value {modulus}")

print(f"Exponentiation value {exponentitation}") 
