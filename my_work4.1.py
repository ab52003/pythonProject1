from fake_math import divide as div_1
from true_math import divide as div_2


first = int(input('Введите число: '))
second = int(input('Введите число: '))

print(div_1(first, second))

print(div_2(first, second))