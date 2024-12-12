import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def days (self, day):
        self.day = day
        if len(str(self.day)) == 1:
            if self.day == 1:
                day1 = 'день'
            elif self.day == 2 or self.day == 3 or self.day == 4:
                day1 = 'дня'
            else:
                day1 = 'дней'
        else:
            num_1 = int(str(self.day)[-1])
            num_2 = int(str(self.day)[-2])
            if num_1 == 1 and num_2 != 1:
                day1 = 'день'
            elif (num_1 == 2 and num_2 != 1) or (num_1 == 3 and num_2 != 1) or (num_1 == 4 and num_2 != 1):
                day1 = 'дня'
            else:
                day1 = 'дней'
        return day1

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100
        day = 0
        day1 = ''
        while enemy:
            time.sleep(1)
            enemy = enemy - self.power
            day1 = self.days(day+1)
            day += 1
            print(f'{self.name} сражается {day} {day1}, осталось {enemy} воинов.')
        print(f'{self.name} одержал победу спустя {day} {day1}!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')