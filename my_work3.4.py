def single_root_words(root_word, *other_word): # объявление функции
    global same_words # объявление глобальной переменной
    same_words = [] # пустой список
    root_word = root_word.lower() # перевод строки в нижний регистр
    other_word = [x.lower() for x in other_word] # перевод списка в нижний регистр
    for i in other_word: # цикл
        if root_word in i: # проверка нахождения слова в словах из списка
            same_words.append(i) # добавление слова в список
        elif i in root_word: # проверка нахождения слов из списка в слове
            same_words.append(i) # добавление слова в список


root_word = input('Введите слово: ') # ввод слова
other_word = input('Введите несколько слов: ').split() # ввод нескольких слов

single_root_words(root_word, *other_word) # вызов функции
print(same_words) # вывод на экран списка