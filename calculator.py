# BASIC CALCULATOR PROGRAM

# Ask user for two numbers and an operation_sign
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))
operation_sign = input("Enter operation_sign (+(addition), -(substraction), *(multiplication), /(division)): ")

# Codes to perform the operation_sign
if operation_sign == "+(addition)":
    result = num_1 + num_2
    print(f"{num_1} + {num_2} = {result}")
elif operation_sign == "-(substraction)":
    result = num_1 - num_2
    print(f"{num_1} - {num_2} = {result}")
elif operation_sign == "*(multiplication)":
    result = num_1 * num_2
    print(f"{num_1} * {num_2} = {result}")
elif operation_sign == "/(division)":
    if num_2 != 0:
        result = num_1 / num_2
        print(f"{num_1} / {num_2} = {result}")
    else:
        print("Error: Division by zero is not allowed, Input a valid number.")
else:
    print("Invalid operation. Please choose +(addition), -(substraction), *(multiplication), /(division)")
