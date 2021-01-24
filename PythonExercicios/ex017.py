# 017: Make a program that calculates the hypotenuse from triangle sides

from math import sqrt, pow

opps = float(input("Write the length of opposite side: "))
adja = float(input("Now the adjacent side: "))
hyp = sqrt(pow(opps, 2) + pow(adja, 2))
print(f"The hypotenuse of your sides is {hyp:.2f}")
