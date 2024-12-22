import multiprocessing
from multiprocessing import Pool
import time
import threading

def read_info(*name):
    all_data = []
    name =  ''.join(name)
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            data = file.readline()
            all_data.append(data)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start_time = time.perf_counter()
for name in filenames:
    thread = threading.Thread(target=read_info, args=name)
    thread.start()
end_time = time.perf_counter()
elapsed_time = (end_time - start_time)
print(f'Работа функции {elapsed_time}')

#start_time = time.perf_counter()
#if __name__ == '__main__':
    #for name in filenames:
        #process = multiprocessing.Process(target=read_info, args=(name))
        #process.start()
#end_time = time.perf_counter()
#elapsed_time = end_time - start_time
#print(f'Работа функции {elapsed_time}')


#start_time = time.perf_counter()
#if __name__ == '__main__':
    #with Pool(processes=5) as pool:
        #res = pool.map(read_info, filenames)
#end_time = time.perf_counter()
#lapsed_time = end_time - start_time
#print(f'Работа функции {elapsed_time}')