calls = 0 # счетчик

def count_calls(): # Функция count_calls
    global calls # глобальная переменная
    calls = calls + 1 # увеличение счетчика

def string_info(string): # Функция string_info
    print(len(string), string.upper(), string.lower()) # вывод на экран кортежа из: длины строки, строки в верхнем регистре, строки в нижнем регистре
    count_calls() # вызов функции count_calls

def is_contains(string, list_to_search): # Функция is_contains
    string.lower() # перевод строки в нижний регистр
    list_to_search = [x.lower() for x in list_to_search] # перевод списка в нижний регистр
    print(string in list_to_search) # вывод на экран результат проверки наличия строки в списке
    count_calls() # вызов функции count_calls

while calls >= 0: # цикл вызова функций
    string = input("Введите слово: ") # ввод строки
    list_to_search = input("Введите список слов: ").split() # ввод списка
    string_info(string) # вызов функции string_info
    is_contains(string, list_to_search) # вызов функции is_contains
    print(calls) # вывод счетчика
    if input("Продолжить (да/нет): ") == 'нет': # условие продолжения цикла
        break # выход из цикла