"""
011: Make a program that reads a wall's width and height in meters,
calculate its area and the how much ink necessary to paint it
"""

width = float(input("What is the width of the wall in meters? "))
height = float(input("Now the height in meters: "))
area = (width * height)
print(f"For a wall of {area}m² will be necessary {area / 2} liters of ink")
