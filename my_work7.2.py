def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    file.seek(0)
    strings_positions = {}
    i = 0
    while i < len(strings):
        a = i + 1
        b = file.tell()
        c = strings[i]
        file.write(strings[i])
        strings_positions[(a,b)] = f'{c}'
        i +=1
    file.close()
    return strings_positions

strings = ['Text for tell.\n', 'Используйте кодировку utf-8.\n', 'Because there are 2 languages!\n', 'Спасибо!\n']

result = custom_write('test.txt', strings)

for item in result.items():
    print(item)