# 018: Make a program that reads an angle and show your sine,cosine and tangent values.

from math import cos, sin, tan, radians

angle = radians(float(input("Write an angle in radians: ")))
print(f"The value of sine, cosine and tangent of angle is: {sin(angle):.2f}, {cos(angle):.2f} and {tan(angle):.2f}")
