# Simple Interest Calculator.

principle = 0
time = 0
rate = 0

while True:
    principle = float(input("Enter the Principle amount: "))
    if principle < 0:
        print("The Principle can't be less than zero")
    else:
        break

while True:
    time = int(input("Enter the Time in years: "))
    if time < 0:
        print("The time can't be less than Zero")
    else:
        break

while True:
    rate = int(input("Enter the Rate: "))
    if rate < 0:
        print("The Rate can't be zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years: ₹{total:.2f}")
