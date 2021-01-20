""" # 015: Make a program that asks the mileage of a car and how many days it was used.
The program needs to show how much necessary will be paid, considering R$60.00 per day and R$0.15 per mile drove.
"""

km = float(input("How many miles did you drive? "))
days = int(input("And how many days? "))

print(f"You are going to pay R${(km * 0.15) + (days * 60)}")
