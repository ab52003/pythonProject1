def print_params(a = 1, b = 'строка', c = True): # объявление функции
    print(a, b, c) # вывод на экран


print_params(1, 'том') # вызов функции с двумя указанными параметрами
print_params(5) # вызов функции с одним указанным параметром
print_params() # вызов функции без указанных параметров

#print_params(b = 25) - ошибка
#print_params(c = [1,2,3]) - ошибка

values_list = [1, 'лес', True] # список с тремя параметрами
values_dict = {'a': 5, 'b': 'поле', 'c': False} # словарь с тремя параметрами
values_list_2 = [5, 'пол'] # список с двумя параметрами

print_params(*values_list) # вызов функции
print_params(**values_dict) # вызов функции
print_params(*values_list_2, 42) # вызов функции