def single_root_words(root_word, *other_word): # объявление функции
    same_words = [] # пустой список
    root_word = root_word.lower() # перевод строки в нижний регистр
    other_word = [x.lower() for x in other_word] # перевод списка в нижний регистр
    for i in other_word: # цикл
        if root_word in i or i in root_word: # проверка нахождения слова в словах из списка
           same_words.append(i) # добавление слова в список
    return same_words # возврат значения


root_word = input('Введите слово: ') # ввод слова
other_word = input('Введите несколько слов: ').split() # ввод нескольких слов

print(single_root_words(root_word, *other_word)) # вызов функции