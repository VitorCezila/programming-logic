# 012: Make a program that reads the price of a product and show the value with 5% off.

prod = float(input("What's the price of that: $"))
print(f"The new price is ${prod - (prod * (5/100)):.2f}")
