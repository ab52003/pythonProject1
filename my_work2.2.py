first = int(float(input())) # ввод первого числа с переводом в целое
second = int(float(input())) # ввод второго числа с переводом в целое
third = int(float(input())) # ввод третьего числа с переводом в целое
if first == second == third: # совпадение всех трех чисел
    print(3)
elif first == second or first == third or second == third: # совпадение только двух из трех чисел
    print(2)
else:  # несовпадение чисел
    print(0)
