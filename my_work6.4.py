class Figure:
    sides_count = 0
    def __init__(self, color, filled = False, *sides):
        self.__sides = sides
        self.__color = color
        self.filled = filled
        self._is_valid_color()
        self._is_valid_sides()
        self.count_sides()


    def get_color(self):
        r = self.__color[0]
        g = self.__color[1]
        b = self.__color[2]
        return r, g, b


    def _is_valid_color(self):
        r = self.__color[0]
        g = self.__color[1]
        b = self.__color[2]
        if r in range(0, 255) and g in range(0, 255) and b in range(0, 255):
            return True
        else:
            return False


    def set_color(self, r, g, b):
        if r in range(0, 255) and g in range(0, 255) and b in range(0, 255):
            self.__color = (r, g, b)
            return self.__color
        else:
            return self.__color


    def _is_valid_sides(self):
        if isinstance(self.__sides, int) is False:
            for i in range(len(self.__sides)):
                if isinstance(self.__sides[i], int) and self.__sides[i] > 0 and len(self.__sides) == self.sides_count:
                    return True
                else:
                    return False
        else:
            if self.__sides > 0 and self.__sides == self.sides_count:
                return True
            else:
                return False


    def get_sides(self):
        return self.__sides


    def  __len__(self):
        self._is_valid_sides()
        if isinstance(self, Circle):
            return self.__sides[0]
        else:
            return sum(self.__sides)


    def set_sides(self, *new_sides):
        self._is_valid_sides()
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides
            return self.__sides
        else:
            return self.__sides


    def count_sides(self):
        if len(self.__sides) == self.sides_count:
            pass
        else:
            i = 1
            list_1 = ()
            while i <= self.sides_count:
                self.__sides = list_1 = (*list_1, 1)
                i += 1
            return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, filled, *sides):
        super().__init__( color, filled, *sides)
        self.__sides = self._Figure__sides

        self.__radius = round(sides[0] / (2 * 3.14), 2)


    def get_radius(self):
        return self.__radius


    def get_square(self):
        s = round(3.14 * (self.__radius ** 2), 2)
        return s


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, filled, *sides):
        super().__init__(color, filled, *sides)
        self.__sides = self._Figure__sides

    def get_square(self):
        a = self.__sides[0]
        b = self.__sides[1]
        c = self.__sides[2]
        p = (a + b + c)/2
        s = round((p * (p - a) * (p - b) * (p - c)) ** (0.5), 2)
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, filled, *sides):
        super().__init__(color, filled, *sides)
        self.__sides = self._Figure__sides


    def get_volume(self):
        v = round(self.__sides[0] ** 3, 2)
        return v



circle1 = Circle((200, 200, 100), False, 10)  # (Цвет, стороны)

cube1 = Cube((222, 35, 130), False, 20, 10)

triangl1 = Triangle((222, 35, 130), False, 20, 35, 30)

print(circle1.get_color())
print(circle1.set_color(200, 250, 100))
print(circle1.get_color())
print(circle1.set_color(200, 250, 500))
print(circle1.get_color())
print(circle1.get_radius())
print(circle1.__len__())
print(triangl1.__len__())
print(cube1.get_sides())
print(circle1.set_sides(20, 30))
print(circle1.get_sides())
print(circle1.set_sides(50))
print(circle1.get_sides())
print(circle1.get_square())
print(triangl1.get_square())
print(cube1.get_volume())
