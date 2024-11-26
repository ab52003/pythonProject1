def add_everything_up(a, b):
    try:
        c = round(a + b, 2)
        return c
    except TypeError:
        c = str(a) + str(b)
        return c


print(add_everything_up(123.456, 'строка'))

print(add_everything_up('яблоко', 4215))

print(add_everything_up(123.456, 7))