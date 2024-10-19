def calculate_structure_sum(data_structure):
    global result
    for i in data_structure:
        if type(i) == str:
            result += len(i)
        elif type(i) == int:
            result += i
        elif type(i) == list:
            for j in i:
                if type(j) == str:
                    result += len(j)
                elif type(j) == int:
                    result += j
                elif type(j) == list or type(j) == set or type(j) == dict or type(j) == tuple:
                    calculate_structure_sum(j)
        elif type(i) == dict:
            for j in dict.keys(i):
                if type(j) == str:
                    result += len(j)
                elif type(j) == int:
                    result += j
            for j in dict.values(i):
                if type(j) == str:
                    result += len(j)
                elif type(j) == int:
                    result += j
        elif type(i) == set:
            for j in i:
                if type(j) == str:
                    result += len(j)
                elif type(j) == int:
                    result += j
                elif type(j) == set or type(j) == list or type(j) == dict or type(j) == tuple:
                    calculate_structure_sum(j)
        elif type(i) == tuple:
            calculate_structure_sum(i)
    return result


result = 0



data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

print(calculate_structure_sum(data_structure))