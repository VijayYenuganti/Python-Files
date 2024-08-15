# Weight Converter.

weight = float(input("Enter Your Weight > "))
unit = input("To which unit you want to convert (K or L) > ")

unit.strip().upper()

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


