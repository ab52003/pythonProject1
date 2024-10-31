class House: # создание класса House
    def __init__(self, name, number_of_floors): # определение метода __init__
        self.name = name # атрибут объекта self.name
        self.number_of_floors = number_of_floors # атрибут объекта self.number_of_floors


    def go_to(self, new_floor): # создание метода go_to с параметром new_floor
        i = 1 # счетчик
        if new_floor < i or new_floor > self.number_of_floors: # несуществующий этаж
            print('"В', self.name, 'такого этажа не существует"') # ссообщение о несуществующем этаже
        else:
            for i in range(1, new_floor + 1): # перебо этажей
                print(i) # номер очередного этажа
                i += 1 # увеличение счетчика


h1 = House('ЖК Черемушки', 18) # первый объект класса House

h2 = House('ЖК Кленовая аллея', 2) # второй объект класса House

a = input('Введите число: ') # ввод номера этажа

h1.go_to(int(a)) # вызов метода go_to для первого объекта

a = input('Введите число: ') # ввод номера этажа

h2.go_to(int(a)) # вызов метода go_to для второго объекта