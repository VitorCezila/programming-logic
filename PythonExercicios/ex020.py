"""
020: The same professor of the last challenge wants to randomize the presentation order of your student's works.
Make a program that reads the name of four students and show the sorted order.
"""

from random import shuffle

students = "Gabriel Bu Vitor Cezila".split()
shuffle(students)
print(f"The order of presentations is {students}")
