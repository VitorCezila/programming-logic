"""
020: The same professor of the last challenge wants to randomize the presentation order of your student's works.
Make a program that reads the name of four students and show the sorted order.
"""

from random import shuffle

student1 = input("What's the name of the first student?: ")
student2 = input("And of the second one? ")
student3 = input("And of the third one? ")
listS = [student1, student2, student3]
shuffle(listS)
print(f"The order of presentations is {listS}")
