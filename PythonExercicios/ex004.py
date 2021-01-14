# 004: Make a program that reads something and shows your data type and all possible information.

x = input('Type something: ')

print(f'The primitive type of {x} is {type(x)}')
print(f'Is {x} alpha? {x.isalpha()}')
print(f'Is it numeric? {x.isnumeric()}')
print(f'Is it alphanumeric? {x.isalnum()}')
print(f'Is it upper case? {x.isupper()}')
print(f'Is it lower case? {x.islower()}')
print(f'Is it title? {x.istitle()}')
print(f'Does it have only space? {x.isspace()}')
