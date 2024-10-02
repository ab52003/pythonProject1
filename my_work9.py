grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students) # сортировка множества students c переводом в список
s_0 = sorted_students[0] # первый элемент списка sorted_students
s_1 = sorted_students[1] # второй элемент списка sorted_students
s_2 = sorted_students[2] # третий элемент списка sorted_students
s_3 = sorted_students[3] # четвертый элемент списка sorted_students
s_4 = sorted_students[4] # пятый элемент списка sorted_students
a_0 = grades[0] # первый элемент списка grades
a_0 = sum(a_0)/len(a_0) # среднее значение элементов первого элемента списка grades
a_1 = grades[1] # второй элемент списка grades
a_1 = sum(a_1)/len(a_1) # среднее значение элементов второго элемента списка grades
a_2 = grades[2] # третий элемент списка grades
a_2 = sum(a_2)/len(a_2) # среднее значение элементов третьего элемента списка grades
a_3 = grades[3] # четвертый элемент списка grades
a_3 = sum(a_3)/len(a_3) # среднее значение элементов четвертого элемента списка grades
a_4 = grades[4] # пятый элемент списка grades
a_4 = sum(a_4)/len(a_4) # среднее значение элементов пятого элемента списка grades
slovar = {} # создание пустого словаря
slovar.update({s_0: a_0, s_1: a_1, s_2: a_2, s_3: a_3, s_4: a_4}) # добавление элементов в словарь
print(slovar) # вывод на экран словаря