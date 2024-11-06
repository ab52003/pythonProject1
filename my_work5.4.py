class House: # создание класса House

    houses_history = []  # атрибут класса houses_history


    def __new__(cls, *args): # определение метода __new__
        cls.houses_history.append(args[0]) # добавление наименование объекта в список houses_history
        return object.__new__(cls) # возвращает новое значение


    def __init__(self, name, number_of_floors): # определение метода __init__
        self.name = name # атрибут объекта self.name
        self.number_of_floors = number_of_floors # атрибут объекта self.number_of_floors


    def __len__(self): # создание метода len
        return (self.number_of_floors) # возвращает кол-во этажей здания


    def __str__(self): # создание метода str
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}' # возвращает строку


    def __eq__(self, other): # создание метода eq (перегрузка оператора ==)
        return self.number_of_floors == other.number_of_floors # возвращает результат сравнения кол-ва этажей зданий


    def __lt__(self, other): # создание метода lt (перегрузка оператора <)
        return self.number_of_floors < other.number_of_floors # возвращает срвнение кол-ва этажей здания


    def __le__(self, other): # создание метода le (перегрузка оператора <=)
        return self.number_of_floors <= other.number_of_floors # возвращает срвнение кол-ва этажей здания


    def __gt__(self, other): # создание метода gt (перегрузка оператора >)
        return self.number_of_floors > other.number_of_floors # возвращает срвнение кол-ва этажей здания


    def __ge__(self, other): # создание метода ge (перегрузка оператора >=)
        return self.number_of_floors >= other.number_of_floors # возвращает срвнение кол-ва этажей здания


    def __ne__(self, other): # создание метода ne (перегрузка оператора !=)
        return self.number_of_floors != other.number_of_floors # возвращает срвнение кол-ва этажей здания


    def __add__(self, value): # создание метода add (перегрузка оператора +)
        self.number_of_floors = self.number_of_floors + value # увеличение количества этажей
        return self # возвращает объект с измененным значением


    def __radd__(self, value): # создание метода radd (перегрузка оператора +)
        self.number_of_floors += value # увеличение количества этажей
        return self # возвращает объект с измененным значением


    def __iadd__(self, value): # создание метода iadd (перегрузка оператора +)
        self.number_of_floors = value + self.number_of_floors # увеличение количества этажей
        return self # возвращает объект с измененным значением


    def __del__(self): # создание метода del (перегрузка оператора del)
        House.houses_history.remove(self.name) # удаляет наименование объекта из списка
        return print(f'{self.name}, снесён, но он останется в истории') # возвращает вывод на экран строки


    #def del_del (self): # создание метода del_del
        #House.houses_history.remove(self.name) # удаляет наименование объекта из списка
        #return print(f'{self.name}, снесён, но он останется в истории') # возвращает вывод на экран строки


    def is_in (self, args): # создание метода проверки на числовое значение
        if not all(ch.isdigit() for ch in str(args)): # если не введено число
            return print("Число не введено") # вернуть сообщение
        elif not(isinstance(args, int)): # если значение не числовое
            return int(args) # возвращает числовое значение
        else:
            return args # возвращает исходное значение


    def go_to(self, new_floor): # создание метода go_to с параметром new_floor
        if new_floor < 1 or new_floor > self.number_of_floors: # несуществующий этаж
            print('"В', self.name, 'такого этажа не существует"') # сообщение о несуществующем этаже
        else:
            for i in range(1, new_floor + 1): # перебор этажей
                print(i) # номер очередного этажа


h1 = House('ЖК Черемушки', '6') # первый объект класса House
print(House.houses_history) # вывод на экран списка

h2 = House('ЖК Кленовая аллея', 7) # второй объект класса House
print(House.houses_history) # вывод на экран списка

h3 = House('ЖК Дубки', 8) # третий объект класса House
print(House.houses_history) # вывод на экран списка

h1.number_of_floors = h1.is_in(h1.number_of_floors) # вызов проверки на числовое значение
h2.number_of_floors = h2.is_in(h2.number_of_floors) # вызов проверки на числовое значение
h3.number_of_floors = h3.is_in(h3.number_of_floors) # вызов проверки на числовое значение

print(str(h1)) # вызов метода str для первого объекта c выводом на экран
print(str(h2)) # вызов метода str для второго объекта c выводом на экран
print(str(h3)) # вызов метода str для третьего объекта c выводом на экран

print(len(h1)) # вызов метода len для первого объекта c выводом на экран
print(len(h2)) # вызов метода len для второго объекта c выводом на экран
print(len(h3)) # вызов метода len для третьего объекта c выводом на экран

h1.go_to(h1.is_in(input('Введите число: '))) # вызов метода go_to для первого объекта

h2.go_to(h2.is_in(input('Введите число: '))) # вызов метода go_to для второго объекта

h3.go_to(h3.is_in(input('Введите число: '))) # вызов метода go_to для третьего объекта

del h3 # вызов метода del
#h3.del_del () # вызов метода del_del
print(House.houses_history) # вывод на экран списка

print(h1 == h2) # вызов метода eq
print(h1 < h2) # вызов метода lt
print(h1 <= h2) # вызов метода le
print(h1 > h2) # вызов метода gt
print(h1 >= h2) # вызов метода ge
print(h1 != h2) # вызов метода ne

h1.__add__(h1.is_in(input('Введите число: '))) # вызов метода add
print(len(h1)) # вызов метода len для первого объекта c выводом на экран

h2.__add__(h2.is_in(input('Введите число: '))) # вызов метода add
print(len(h2)) # вызов метода len для второго объекта c выводом на экран

h1.__radd__(h1.is_in(input('Введите число: '))) # вызов метода add
print(len(h1)) # вызов метода len для первого объекта c выводом на экран

h2.__radd__(h2.is_in(input('Введите число: '))) # вызов метода add
print(len(h2)) # вызов метода len для второго объекта c выводом на экран

h1.__iadd__(h1.is_in(input('Введите число: '))) # вызов метода add
print(len(h1)) # вызов метода len для первого объекта c выводом на экран

h2.__iadd__(h2.is_in(input('Введите число: '))) # вызов метода add
print(len(h2)) # вызов метода len для второго объекта c выводом на экран