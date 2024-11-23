import os.path
import time

for root, dirs, files in os.walk('.'):

  for file in files:

    filepath =  os.path.join(os.getcwd())

    filetime = os.path.getmtime(os.getcwd())

    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

    filesize = os.path.getsize(os.getcwd())

    parent_dir = os.path.dirname(os.getcwd())

    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')