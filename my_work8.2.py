def  personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for i in range(len(numbers)):
            try:
                result += numbers[i]
            except TypeError:
                incorrect_data += 1
        return (result, incorrect_data)
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


def calculate_average(numbers):
    a = personal_sum(numbers)
    num = 0
    calc = 0
    try:
        for i in numbers:
            if isinstance(i, int):
                num += 1
        try:
            calc = a[0]/num
            return calc
        except ZeroDivisionError:
            print('Некорректный тип данных для подсчёта суммы')
            return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


#print(f'Результат 1: {personal_sum("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип

#print(f'Результат 2: {personal_sum([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3

#print(f'Результат 3: {personal_sum(567)}') # Передана не коллекция

#print(f'Результат 4: {personal_sum([42, 15, 36, 13])}') # Всё должно работать


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип

print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3

print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция

print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать