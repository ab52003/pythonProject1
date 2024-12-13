import threading
import time
import random

lock = threading.Lock()

class Bank(threading.Thread):
    def __init__(self, balance):
        threading.Thread.__init__(self)
        self.balance = balance


    def deposit (self):
        lock.acquire()
        for i in range(100):
            time.sleep(0.001)
            rand = random.randint(50, 500)
            self.balance += rand
            print(f'Пополнение: {rand}. Баланс: {self.balance}\n')
            if self.balance >= 500 and lock.locked():
                lock.release()


    def take (self):
        try:
            lock.acquire()
            for i in range(100):
                time.sleep(0.001)
                rand = random.randint(50, 500)
                print(f'Запрос на {rand}\n')
                if rand <= self.balance:
                    self.balance -= rand
                    print(f'Снятие: {rand}. Баланс: {self.balance}\n')
                else:
                    print('Запрос отклонён, недостаточно средств\n')
                    lock.acquire()
        except Exception:
            pass


bk = Bank(500)
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')