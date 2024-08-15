# Python Calculator.

operator = input("Enter an Operator: (+, -, *, /, %) > ")

operator.strip()

num1 = eval(input("Enter 1st Number > "))
num2 = eval(input("Enter 2nd Number > "))


if operator == "+":
    result = num1 + num2
    print(f"Result: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"Result: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"Result: {result}")
elif operator == "/":
    result = num1 / num2
    print(f"Result: {round(result, 3)}")
elif operator == "%":
    result = num1 % num2
    print(f"Result: {round(result, 3)}")
else:
    print(f"{operator} Please! Select Correct Operator.")
