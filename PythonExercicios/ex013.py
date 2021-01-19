# Make a program that reads the salary of someone and shows the salary with a 15% increase.

salary = float(input("What's your salary? $"))
print(f"Congratulations!! Now your salary is ${salary + (salary * (15/100)):.2f}")
