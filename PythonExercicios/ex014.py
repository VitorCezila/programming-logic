# 014: Make a program that converts C° to Fahrenheit

graus = int(input("Write a temperature in C°: "))
print(f"{graus}°C in Fahrenheit is {(graus * (9/5) + 32):.1f}°F")
