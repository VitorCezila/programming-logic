# 019: Make a program that randomizes one of four students to clean the blackboard.

from random import choice

students = ["Gabriel", "Vitor", "Bu", "Cezila"]
print(f"The student that will clean the blackboard is {choice(students)}")
