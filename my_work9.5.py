class StepValueError(ValueError):
    pass

class BorderValueError(ValueError):
    pass

class Iterator():

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        self.stop = stop + 1 if step > 0 else stop - 1
        if self.step == 0:
            raise StepValueError('шаг не может быть равен 0')
        elif (self.start > self.stop and self.step > 0) or (self.start < self.stop and self.step < 0):
            raise BorderValueError('неверно заданы параметры диапазона')

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer >= self.stop) or (self.step < 0 and self.pointer <= self.stop):
            raise StopIteration
        current = self.pointer
        self.pointer += self.step
        return current


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
except BorderValueError:
    print('Границы указаны неверно')
print()

try:
    iter2 = Iterator(-5, 1)
    for i in iter2:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
except BorderValueError:
    print('Границы указаны неверно')
print()

try:
    iter3 = Iterator(6, 15, 2)
    for i in iter3:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
except BorderValueError:
    print('Границы указаны неверно')
print()

try:
    iter4 = Iterator(5, 1, -1)
    for i in iter4:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
except BorderValueError:
    print('Границы указаны неверно')
print()

try:
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
except BorderValueError:
    print('Границы указаны неверно')
print()


