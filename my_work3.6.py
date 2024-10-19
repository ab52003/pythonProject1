def calculate_structure_sum(data_structure):
    global result
    for i in data_structure:
        if isinstance(i, str):
            result += len(i)
        elif isinstance(i, int):
            result += i
        elif isinstance(i, list):
            for j in i:
                if isinstance(j, str):
                    result += len(j)
                elif isinstance(j, int):
                    result += j
                elif isinstance(j, list | set | dict | tuple):
                    calculate_structure_sum(j)
        elif isinstance(i, dict):
            for j in dict.keys(i):
                if isinstance(j, str):
                    result += len(j)
                elif isinstance(j, int):
                    result += j
            for j in dict.values(i):
                if isinstance(j, str):
                    result += len(j)
                elif isinstance(j, int):
                    result += j
        elif isinstance(i, set):
            for j in i:
                if isinstance(j, str):
                    result += len(j)
                elif isinstance(j, int):
                    result += j
                elif isinstance(j, list | set | dict | tuple):
                    calculate_structure_sum(j)
        elif isinstance(i, tuple):
            calculate_structure_sum(i)
    return result


result = 0

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

print(calculate_structure_sum(data_structure))