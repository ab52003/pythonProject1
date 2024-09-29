immutable_var = (1, "res", 5, 2.2) # создание кортежа
print("Immutable tuple:", immutable_var) # вывод на консоль кортежа
#immutable_var[1] = 14 # попытка замены элемента кортежа - TypeError: 'tuple' object does not support item assignment - кортеж не поддерживает обращение по элементам
mutable_list = [8, "res", 5, 2.8] # создание списка
print("Mutable list:", mutable_list) # вывод на консоль списка
mutable_list[1] = 14 # замена второго элемента списка
mutable_list.append(555) # добавление элемента в список
mutable_list.extend(["plane", 11]) # добавление двух элементов в список
mutable_list.remove(5) # удаление элемента из списка
print("Mutable list modified:", mutable_list) # вывод на консоль измененного списка
