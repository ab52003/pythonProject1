from random import random

#area = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] # исходный список
from operator import itemgetter, attrgetter, methodcaller
n = int(input("Введите число от 3 до 20: ")) # ввод числа
list = [] # создание пустого списка
for i in range(1, n): # цикл - перебор чисел до введенного числа
    for j in range(1, i): # второй цикл - перебор числел внутри первого цикла
        if i != j and n % (i + j) == 0: # условие проверки числа
            if i < j: # условие проверки меньшего числа
                list.append([i, j]) # добавление пары элементов в список
            elif j < i: # условие проверки меньшего числа
                list.append([j, i])  # добавление пары элементов в список
list = sorted(list, key=itemgetter(0, 1)) # сортировка списка
a = len(list) # длина списка
i = 0 # счетчик цикла
list1 = [] # новый список
while i < a: # цикл - разбивка пар чисел на отдельные числа
    list1.append(list[i][0]) # добавление первого числа из пары в новый список
    list1.append(list[i][1]) # добавление второго числа из пары в новый список
    i = i + 1 # увеличение счетчика цикла
print(n, '- число из первой вставки') # вывод на экран введенного числа
print(*list1, '- нужный пароль') # вывод на экран паролей