def res(item): # функция подсчета строк и целых чисел вспомогательная
    global result # глобальная переменная
    if isinstance(item, str): # если строка
        result += len(item)
    elif isinstance(item, int): # если число
        result += item


def calculate_structure_sum(data_structure): # функция подсчета основная
    global result # глобальная переменная
    for i in data_structure: # цикл первичный
        res(i) # вызов вспомогательной функции
        if isinstance(i, list): # если обнаружен список
            for j in i: # цикл вторичный (список)
                res(j) # вызов вспомогательной функции
                if isinstance(j, list | set | dict | tuple): # если обнаружены вложения
                    calculate_structure_sum(j) # рекурсия
        elif isinstance(i, dict): # если обнаружен словарь
            for j in dict.keys(i): # цикл вторичный (словарь, ключи)
                res(j) # вызов вспомогательной функции
            for j in dict.values(i): # цикл вторичный (словарь, значения)
                res(j) # вызов вспомогательной функции
        elif isinstance(i, set): # если обнаружено множество
            for j in i: # цикл вторичный (смножество)
                res(j) # вызов вспомогательной функции
                if isinstance(j, list | set | dict | tuple): # если обнаружены вложения
                    calculate_structure_sum(j) # рекурсия
        elif isinstance(i, tuple): # если обнаружен кортеж
            calculate_structure_sum(i) # рекурсия
    return result # возврат переменной


result = 0 # объявление переменной

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

print(calculate_structure_sum(data_structure))