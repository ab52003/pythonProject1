def test_function(x): # объявление первой функции
    d = x ** 2 # вычисление переменной
    def inner_function(): # объявление второй функции
        print('"Я в области видимости функции test_function"') # печать значения второй функции
    inner_function() # вызов второй функции
    return d # возврат переменной


x = int(input('Введите число: ')) # ввод числа

print(test_function(x)) # вызов первой функции с печатью возвращаемой переменной

inner_function() # вызов второй функции вне первой функции (выводит ошибку)