# 016: Make a program that reads a float and return an integer.
from math import trunc

real = float(input("Write a integer number: "))
print(f"The integer part is: {trunc(real)}")
