from queue import Queue
from queue import Empty
import threading
import time

class Table:
    guest = None
    def __init__(self, number):
        self.number = number

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(3,10):
            time.sleep(i)

class Cafe:
    queue = Queue()
    def __init__(self, *tables):
        self.tables = tables


    def guest_arrival(self, *guests):
        cafe = []
        tab = []
        for table in self.tables:
            for guest in guests:
                if table.guest is None and guest.name not in tab:
                    table.guest = guest.name
                    tab.append(guest.name)
                    ges_guest = Guest(Guest.name)
                    ges_guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}\n')
                    if guest.name in cafe:
                        table.guest = Cafe.queue.get()
                elif guest.name in cafe or guest.name in tab:
                    pass
                else:
                    Cafe.queue.put(guest.name)
                    cafe.append(guest.name)
                    print(f'{guest.name} в очереди\n')


    def discuss_guests(self):
        while not Cafe.queue.empty():
            for table in self.tables:
                if not table.guest is None:
                    if not Guest(Guest.name).is_alive():
                        print(f'{table.guest} покушал(-а) и ушёл(ушла)\n')
                        print(f'Стол номер {table.number} свободен\n')
                        table.guest = None
                        try:
                            table.guest = Cafe.queue.get(timeout=10)
                            print(f'{table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}\n')
                        except Empty:
                            break



tables = [Table(number) for number in range(1, 6)]

guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)

cafe.guest_arrival(*guests)

cafe.discuss_guests()