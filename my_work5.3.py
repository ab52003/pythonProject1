class House: # создание класса House
    def __init__(self, name, number_of_floors): # определение метода __init__
        self.name = name # атрибут объекта self.name
        self.number_of_floors = number_of_floors # атрибут объекта self.number_of_floors


    def __len__(self): # создание метода len
        return (self.number_of_floors) # возвращает кол-во этажей здания


    def __str__(self): # создание метода str
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}' # возвращает строку


    def __eq__(self, other): # создание метода eq (перегрузка оператора ==)
        if not(isinstance(other.number_of_floors, int)): # если значение не числовое
            return "Число не введено" # вернуть сообщение
        elif not(isinstance(other, House)): # если объект не типа House
            return "Это не  объект типа House" # вернуть сообщение
        else:
            return self.number_of_floors == other.number_of_floors # возвращает результат сравнения кол-ва этажей зданий


    def __lt__(self, other): # создание метода lt (перегрузка оператора <)
        if not(isinstance(other.number_of_floors, int)): # если значение не числовое
            return "Число не введено" # вернуть сообщение
        elif not(isinstance(other, House)): # если объект не типа House
            return "Это не  объект типа House" # вернуть сообщение
        else:
            return self.number_of_floors < other.number_of_floors # возвращает сравнение кол-ва этажей здания


    def __le__(self, other): # создание метода le (перегрузка оператора <=)
        if not (isinstance(other.number_of_floors, int)):  # если значение не числовое
            return "Число не введено"  # вернуть сообщение
        elif not (isinstance(other, House)):  # если объект не типа House
            return "Это не  объект типа House"  # вернуть сообщение
        else:
            return self.number_of_floors <= other.number_of_floors # возвращает сравнение кол-ва этажей здания


    def __gt__(self, other): # создание метода gt (перегрузка оператора >)
        if not (isinstance(other.number_of_floors, int)):  # если значение не числовое
            return "Число не введено"  # вернуть сообщение
        elif not (isinstance(other, House)):  # если объект не типа House
            return "Это не  объект типа House"  # вернуть сообщение
        else:
            return self.number_of_floors > other.number_of_floors # возвращает сравнение кол-ва этажей здания


    def __ge__(self, other): # создание метода ge (перегрузка оператора >=)
        if not (isinstance(other.number_of_floors, int)):  # если значение не числовое
            return "Число не введено"  # вернуть сообщение
        elif not (isinstance(other, House)):  # если объект не типа House
            return "Это не  объект типа House"  # вернуть сообщение
        else:
            return self.number_of_floors >= other.number_of_floors # возвращает сравнение кол-ва этажей здания


    def __ne__(self, other): # создание метода ne (перегрузка оператора !=)
        if not (isinstance(other.number_of_floors, int)):  # если значение не числовое
            return "Число не введено"  # вернуть сообщение
        elif not (isinstance(other, House)):  # если объект не типа House
            return "Это не  объект типа House"  # вернуть сообщение
        else:
            return self.number_of_floors != other.number_of_floors # возвращает сравнение кол-ва этажей здания


    def __add__(self, value): # создание метода add (перегрузка оператора +)
        if not (isinstance(self.number_of_floors, int)):  # если значение не числовое
            return "Число не введено"  # вернуть сообщение
        else:
            self.number_of_floors = self.number_of_floors + value # увеличение количества этажей
            return self # возвращает объект с измененным значением


    def __radd__(self, value): # создание метода radd (перегрузка оператора +)
        if not (isinstance(self.number_of_floors, int)):  # если значение не числовое
            return "Число не введено"  # вернуть сообщение
        else:
            self.number_of_floors += value # увеличение количества этажей
            return self # возвращает объект с измененным значением


    def __iadd__(self, value): # создание метода iadd (перегрузка оператора +)
        if not (isinstance(self.number_of_floors, int)):  # если значение не числовое
            return "Число не введено"  # вернуть сообщение
        else:
            self.number_of_floors = value + self.number_of_floors # увеличение количества этажей
            return self # возвращает объект с измененным значением


    def go_to(self, new_floor): # создание метода go_to с параметром new_floor
        if new_floor < 1 or new_floor > self.number_of_floors: # несуществующий этаж
            print('"В', self.name, 'такого этажа не существует"') # сообщение о несуществующем этаже
        else:
            for i in range(1, new_floor + 1): # перебор этажей
                print(i) # номер очередного этажа

h1 = House('ЖК Черемушки', 18) # первый объект класса House

h2 = House('ЖК Кленовая аллея', 2) # второй объект класса House

print(str(h1)) # вызов метода str для первого объекта c выводом на экран
print(str(h2)) # вызов метода str для второго объекта c выводом на экран

print(len(h1)) # вызов метода len для первого объекта c выводом на экран
print(len(h2)) # вызов метода len для второго объекта c выводом на экран

a = input('Введите число: ') # ввод номера этажа

h1.go_to(int(a)) # вызов метода go_to для первого объекта

a = input('Введите число: ') # ввод номера этажа

h2.go_to(int(a)) # вызов метода go_to для второго объекта

print(h1 == h2) # вызов метода eq
print(h1 < h2) # вызов метода lt
print(h1 <= h2) # вызов метода le
print(h1 > h2) # вызов метода gt
print(h1 >= h2) # вызов метода ge
print(h1 != h2) # вызов метода ne

a = input('Введите число: ') # ввод числа этажей
h1.__add__(int(a)) # вызов метода add
print(len(h1)) # вызов метода len для первого объекта c выводом на экран

a = input('Введите число: ') # ввод числа этажей
h2.__add__(int(a)) # вызов метода add
print(len(h2)) # вызов метода len для второго объекта c выводом на экран

a = input('Введите число: ') # ввод числа этажей
h1.__radd__(int(a)) # вызов метода add
print(len(h1)) # вызов метода len для первого объекта c выводом на экран

a = input('Введите число: ') # ввод числа этажей
h2.__radd__(int(a)) # вызов метода add
print(len(h2)) # вызов метода len для второго объекта c выводом на экран

a = input('Введите число: ') # ввод числа этажей
h1.__iadd__(int(a)) # вызов метода add
print(len(h1)) # вызов метода len для первого объекта c выводом на экран

a = input('Введите число: ') # ввод числа этажей
h2.__iadd__(int(a)) # вызов метода add
print(len(h2)) # вызов метода len для второго объекта c выводом на экран