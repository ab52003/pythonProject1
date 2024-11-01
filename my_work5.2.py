class House: # создание класса House
    def __init__(self, name, number_of_floors): # определение метода __init__
        self.name = name # атрибут объекта self.name
        self.number_of_floors = number_of_floors # атрибут объекта self.number_of_floors


    def go_to(self, new_floor): # создание метода go_to с параметром new_floor
        if new_floor < 1 or new_floor > self.number_of_floors: # несуществующий этаж
            print('"В', self.name, 'такого этажа не существует"') # ссообщение о несуществующем этаже
        else:
            for i in range(1, new_floor + 1): # перебор этажей
                print(i) # номер очередного этажа
                i += 1 # увеличение счетчика


    def __len__(self): # создание метода len
        return (self.number_of_floors) # возвращает кол-во этажей здания


    def __str__(self): # создание метода str
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}' # возвращает строку


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