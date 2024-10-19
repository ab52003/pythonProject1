def res(item):
    global result
    if isinstance(item, str):
        result += len(item)
    elif isinstance(item, int):
        result += item


def calculate_structure_sum(data_structure):
    global result
    for i in data_structure:
        res(i)
        if isinstance(i, list):
            for j in i:
                res(j)
                if isinstance(j, list | set | dict | tuple):
                    calculate_structure_sum(j)
        elif isinstance(i, dict):
            for j in dict.keys(i):
                res(j)
            for j in dict.values(i):
                res(j)
        elif isinstance(i, set):
            for j in i:
                res(j)
                if isinstance(j, list | set | dict | tuple):
                    calculate_structure_sum(j)
        elif isinstance(i, tuple):
            calculate_structure_sum(i)
    return result


result = 0

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

print(calculate_structure_sum(data_structure))