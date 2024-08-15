# Weight Converter.

weight = float(input("Enter Your Weight > "))
unit = input("To which unit you want to convert (K or L) > ").upper()

if unit == "K":
    weight /= 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
elif unit == "L":
    weight *= 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
else:
    print(f"Enter Valid Units.")

