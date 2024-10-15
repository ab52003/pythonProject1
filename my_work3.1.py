calls = 0 # счетчик

def count_calls(): # Функция count_calls
    global calls # глобальная переменная
    calls = calls + 1 # увеличение счетчика

def string_info(string): # Функция string_info
    count_calls() # вызов функции count_calls
    return len(string), string.upper(), string.lower() # возврат значений

def is_contains(string, list_to_search): # Функция is_contains
    string = string.lower() # перевод строки в нижний регистр
    list_to_search = [x.lower() for x in list_to_search] # перевод списка в нижний регистр
    count_calls() # вызов функции count_calls
    a = 0 # счетчик
    for item in list_to_search: # цикл проверки совпадений
        if string in item: # проверка совпадений в элементах списка
            a = a + 1 # увеличение счетчика
    if a > 0: # проверка счетчика
        return 'True' # возврат значения
    else: # иначе
        return 'False' # возврат значения


while calls >= 0: # цикл вызова функций
    string = input("Введите слово: ") # ввод строки
    list_to_search = input("Введите список слов: ").split() # ввод списка
    print(string_info(string)) # вывод на экран кортежа
    print(is_contains(string, list_to_search)) # вывод на экран результата проверки наличия строки в списке
    print(calls) # вывод на экран счетчика
    if input("Продолжить (да/нет): ") == 'нет':  # условие продолжения цикла
        break  # выход из цикла
