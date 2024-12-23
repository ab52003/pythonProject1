import multiprocessing
from multiprocessing import Pool
import time

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            data = file.readline()
            all_data.append(data)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

#start_time = time.perf_counter()
#for name in filenames:
    #linear = read_info(name)
#end_time = time.perf_counter()
#elapsed_time = (end_time - start_time)
#print(f'Работа функции {elapsed_time}')

if __name__ == '__main__':
    start_time = time.perf_counter()
    with Pool(processes=5) as pool:
        res = pool.map(read_info, filenames)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f'Работа функции {elapsed_time}')