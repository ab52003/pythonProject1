my_string = input()
print(len(my_string)) # количество символов введенного текста
print(my_string.upper()) # верхний регистр
print(my_string.lower()) # нижний регистр
print(my_string.replace(" ","")) # без пробелов
print(my_string[0]) # первый символ
print(my_string[-1]) # последний символ
print(my_string.replace(my_string[0], my_string[0].upper())) # с заглавной буквы