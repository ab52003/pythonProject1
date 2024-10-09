def get_matrix(n, m, value): # объявление функции
    matrix = [] # пустой список
    for i in range(n): # внешний цикл
        matrix.append([]) # добавление пустого списка
        for _ in range(m): # внутренний цикл
            matrix[i].append(value) # добавление value в список
    return matrix # возврат списка
result1 = get_matrix(2, 3, 11) # 1 вариант списка
result2 = get_matrix(2, 5, 12) # 2 вариант списка
result3 = get_matrix(4, 2, 13) # 3 вариант списка
print(result1) # вывод на экран 1 варианта списка
print(result2) # вывод на экран 2 варианта списка
print(result3) # вывод на экран 3 варианта списка