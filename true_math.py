from math import inf

def divide(first, second):
    if first == 0:
        return 'Ошибка'
    elif  second == 0:
        return inf
    else:
        return first/second