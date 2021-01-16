# 006: Make a program that read a number and show your double, triple and your square roots.

n = int(input('Write a number: '))
print(f'The double, triple and square roots of {n} is: {n * 2}, {n * 3} and {(n ** (1/2)):.1f}')
