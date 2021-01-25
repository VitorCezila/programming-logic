# 019: Make a program that randomizes one of four students to clean the blackboard.

from random import choice

student1 = str(input("What's the name of the first student?: "))
student2 = str(input("And of the second one? "))
student3 = str(input("And of the third one? "))
listS = [student1, student2, student3]

print(f"The student that will clean the blackboard is {choice(listS)}")
