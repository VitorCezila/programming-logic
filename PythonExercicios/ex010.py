# 010: Make a program that reads how much money a person have in his wallet and show how many dollars his can buy.

reais = float(input("Type how many reais you have: R$"))
print(f'You can buy: ${(reais / 3.27):.2f}')
