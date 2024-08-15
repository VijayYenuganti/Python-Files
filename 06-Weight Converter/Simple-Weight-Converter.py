# Weight Converter.

try:
    weight = float(input("Enter Your Weight > "))
except ValueError:
    print("Enter the Weight Units in Numeric")


unit = input("To which unit you want to convert (K or L) > ").upper().strip()

if unit == "K":
    weight /= 2.205
    units = "Kgs."
    print(f"Your weight is: {round(weight, 2)} {units}")
elif unit == "L":
    weight *= 2.205
    units = "Lbs."
    print(f"Your weight is: {round(weight, 2)} {units}")
else:
    print(f"{unit} Enter Valid Units.")


