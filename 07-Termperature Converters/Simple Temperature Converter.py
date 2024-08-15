# Temperature Converter

# Get user input for temperature and unit
try:
    temp = float(input("Enter the Temperature > "))
except ValueError:
    print("Invalid temperature value. Please enter a numeric value.")
    exit()

unit = input("Enter Temperature Unit (C/F/K) > ").strip().upper()

# Conversion logic
if unit == "C":
    temp_in_f = round((9 * temp) / 5 + 32, 2)
    temp_in_k = round(temp + 273.15, 2)
    print(f"The temperature in Fahrenheit: {temp_in_f}°F")
    print(f"The temperature in Kelvin: {temp_in_k}K")
elif unit == "F":
    temp_in_c = round((temp - 32) * 5 / 9, 2)
    temp_in_k = round(temp_in_c + 273.15, 2)
    print(f"The temperature in Celsius: {temp_in_c}°C")
    print(f"The temperature in Kelvin: {temp_in_k}K")
elif unit == "K":
    temp_in_c = round(temp - 273.15, 2)
    temp_in_f = round((temp_in_c * 9 / 5) + 32, 2)
    print(f"The temperature in Celsius: {temp_in_c}°C")
    print(f"The temperature in Fahrenheit: {temp_in_f}°F")
else:
    print(f"{unit} is not a valid unit. Please enter 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")
