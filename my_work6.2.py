class Vehicle:

    __COLOR_VARIANTS = ['BLACK', 'WHITE', 'RED']


    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color


    def get_model(self, __model):
        return f'Модель: {self.__model}'


    def get_color (self,__color):
        return f'Цвет: {self.__color}'


    def get_horsepower(self,__engine_power):
        return f'Мощность двигателя: {self.__engine_power}'


    def print_info(self):
        print(self.get_model(self))
        print(self.get_horsepower(self))
        print(self.get_color(self))
        print('Владелец:', self.owner)


    def set_color(self, new_color):
        new_color_1 = new_color.upper()
        if new_color_1 in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color_1
            return self.__color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan (Vehicle):
    __PASSENGERS_LIMIT = 5


car_1 = Sedan('Petrov', "Toyota", 1500, 'blue')

car_1.print_info()
car_1.set_color('Pink')
car_1.set_color('Red')
car_1.owner = 'Sidorov'
car_1.print_info()
print(car_1.get_model(car_1))
print(car_1.owner)

