class Figure:
    sides_count = 0
    def __init__(self, __color, filled = False, *__sides):
        self._sides = __sides
        self._color = __color
        self.filled = filled
        self._is_valid_color()
        self._is_valid_sides()
        self.count_sides()


    def get_color(self):
        return self._color


    def _is_valid_color(self):
        if self._color[0] in range(0, 255) and self._color[1] in range(0, 255) and self._color[2] in range(0, 255):
            return True
        else:
            return False


    def set_color(self, r, g, b):
        if r in range(0, 255) and g in range(0, 255) and b in range(0, 255):
            self._color = (r, g, b)
            return self._color
        else:
            return self._color


    def _is_valid_sides(self):
        if isinstance(self._sides, int) is False:
            for i in range(len(self._sides)):
                if isinstance(self._sides[i], int) and self._sides[i] > 0 and len(self._sides) == self.sides_count:
                    return True
                else:
                    return False
        else:
            if self._sides > 0 and self._sides == self.sides_count:
                return True
            else:
                return False


    def get_sides(self):
        return self._sides


    def  _len_(self):
        self._is_valid_sides()
        if isinstance(self, Circle):
            return self._radius
        else:
            return sum(self._sides)


    def set_sides(self, *new_sides):
        self._is_valid_sides()
        if len(new_sides) == self.sides_count:
            self._sides = new_sides
            return self._sides
        else:
            return self._sides


    def count_sides(self):
        if len(self._sides) == self.sides_count:
            pass
        else:
            i = 1
            list_1 = ()
            while i <= self.sides_count:
                self._sides = list_1 = (*list_1, 1)
                i += 1
            return self._sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, filled, *__sides):
        super().__init__( __color, filled, *__sides)

        self._radius = round(self._sides[0] / (2 * 3.14), 2)


    def get_square(self):
        s = round(3.14 * (self._radius ** 2), 2)
        return s


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, filled, *__sides):
        super().__init__(__color, filled, *__sides)


    def get_square(self):
        a = self._sides[0]
        b = self._sides[1]
        c = self._sides[2]
        p = (a + b + c)/2
        s = round((p * (p - a) * (p - b) * (p - c)) ** (0.5), 2)
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, filled, *__sides):
        super().__init__(__color, filled, *__sides)


    def get_volume(self):
        v = round(self._sides[0] ** 3, 2)
        return v



circle1 = Circle((200, 200, 100), False, 10)  # (Цвет, стороны)

cube1 = Cube((222, 35, 130), False, 20, 10)

triangl1 = Triangle((222, 35, 130), False, 20, 35, 30)

print(circle1.get_color())
print(circle1.set_color(200, 250, 100))
print(circle1.get_color())
print(circle1.set_color(200, 250, 500))
print(circle1.get_color())
print(circle1._radius)
print(circle1._len_())
print(triangl1._len_())
print(cube1.get_sides())
print(circle1.set_sides(20, 30))
print(circle1.get_sides())
print(circle1.set_sides(50))
print(circle1.get_sides())
print(circle1.get_square())
print(triangl1.get_square())
print(cube1.get_volume())
