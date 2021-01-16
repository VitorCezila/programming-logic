# ex009: Make a program to read an integer number and show your multiplication table

n1 = int(input('Write an integer number: '))
n2 = 1

while n2 <= 10:
    print(f'{n1} * {n2} = {n1 * n2}')
    n2 += 1
