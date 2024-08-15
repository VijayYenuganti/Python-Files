# Weight Converter.

weight = float(input("Enter Your Weight > "))
unit = input("To which unit you want to convert (K or L) > ").upper()

if unit == "K":
    weight /= 2.205
    in_units = "Kgs."
elif unit == "L":
    weight *= 2.205
    in_units = "Lbs."
else:
    print(f"{unit}Enter Valid Units.")

print(f"Your weight is: {round(weight, 2)} {in_units}")


