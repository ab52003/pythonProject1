import threading
import time
from time import sleep

def wite_words(word_count, file_name):
    for i in range(word_count):
        with open(file_name, 'a', encoding='utf-8') as file:
            time.sleep(0.1)
            str_1 = f'Какое-то слово № {i+1}\n'
            file.write(str_1)
    print(f'Завершилась запись в файл {file_name}')

start_time = time.time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
end_time = time.time()
elapsed_time = end_time - start_time
print(f'Работа функций {elapsed_time}')

start_time = time.time()

thread = threading.Thread(target=wite_words, args=(10, 'example5.txt'))
thread1 = threading.Thread(target=wite_words, args=(30, 'example6.txt'))
thread2 = threading.Thread(target=wite_words, args=(200, 'example7.txt'))
thread3 = threading.Thread(target=wite_words, args=(100, 'example8.txt'))
thread.start()
thread.join()
thread1.start()
thread1.join()
thread2.start()
thread2.join()
thread3.start()
thread3.join()

end_time = time.time()
elapsed_time = end_time - start_time
print(f'Работа потоков {elapsed_time}')