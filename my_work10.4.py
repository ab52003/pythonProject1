import queue
from queue import Queue
import threading
import time

class Table:
    def __init__(self, table, guest = None):
        self.table = table
        self.guest = guest

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
        for table in self.tables:
            for guest in guests:
                if table.guest is None and guest.name not in cafe:
                    table.guest = guest.name
                    ges_guest = Guest('guest.name')
                    ges_guest.start()
                    cafe.append(guest.name)
                    print(f'{guest.name} сел(-а) за стол номер {table.table}\n')
                else:
                    print(f'{guest.name} в очереди\n')
                    Cafe.queue.put(guest.name)

    def discuss_guests(self):
        while not Cafe.queue.empty():
            for table in self.tables:
                if not table.guest is None:
                    if not table.guest.is_alive():
                        print(f'{table.guest} покушал(-а) и ушёл(ушла)\n')
                        print(f'Стол номер {table.table} свободен\n')
                        table.guest = None
                        table.guest = Cafe.queue.get()
                        print(f'{table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.table}\n')


tables = [Table(number) for number in range(1, 6)]

guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)

cafe.guest_arrival(*guests)

cafe.discuss_guests()