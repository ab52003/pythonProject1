def get_multiplied_digits(n): # объявление функции
    if n == 0: # если введен 0
        return 0 # вернуть 0
    elif not all(ch.isdigit() for ch in str(n)): # если не введено число
        return "Число не введено" # вернуть сообщение
    else: # иначе
        str_number = str(int(n)) # удаление 0 из начала числа
        if len(str_number) > 1 and str_number[- 1] == '0': # если число больше одной цифры и оканчивается на 0
            str_number = str_number.rstrip('0') # удаление 0 в конце числа
        first = int(str_number[0]) # первая цифра числа
        if len(str_number) > 1: # если число больше одной цифры
            return first * get_multiplied_digits(int(str_number[1:])) # вернуть произведение значащих цифр
        else: # иначе
            return first # вернуть одну цифру


n = input('Введите число: ') # вввести число
print(get_multiplied_digits(n)) # вызов функции