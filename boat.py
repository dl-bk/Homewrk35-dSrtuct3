# Створіть імітаційну модель «Причал морських катерів».
# Введіть таку інформацію:
# 1. Середній час між появою пасажирів на причалі у різний
# час доби;
# 2. Середній час між появою катерів на причалі у різний час
# доби;
# 3. Тип зупинки катера (кінцева або інша).
# Визначіть:
# 1. Середній час перебування людини на зупинці;
# 2. Достатній інтервал часу між приходами катерів, коли на
# зупинці не більше N людей одночасно;
# 3. Кількість вільних місць у катері є випадковою величиною.
# Вибір необхідних структур даних визначте самостійно.


import time
from datetime import datetime
import random

CAPACITY = 10

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def peek(self):
        if not self.is_empty():
            return self.queue[0]

    def enqueue(self, item, ):
        if not self.is_full():
            self.queue.append(item)
        else:
            print("Черга заповнена")

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def count(self):
        return len(self.queue)

    def show(self):
        if not self.is_empty():
            print("Елементи в черзі")
            for item in self.queue:
                print(f"Елемент {item}")
        else:
            print("Черга порожня")


class Boat:
    def __init__(self, name, capacity, destination) -> None:
        self.name= name
        self.capacity = capacity
        self.destinaton = destination

class Dock:
    def __init__(self, max_pass, max_boats, boat_interval, pass_interval) -> None:
        self.boat_interval = boat_interval
        self.pass_interval = pass_interval
        self.passengers = Queue(max_pass)
        self.boats = Queue(max_boats)
    
    def pass_come(self, i):
        if not self.passengers.is_full():
            print(f"Passenger {i} comes in {datetime.now()}")
            self.passengers.enqueue(f"Passenger{i}")
        else:
            print("Queue for passengers is full")
        
    def boat_come(self, i):
        destination = ["other", "end"]
        if not self.boats.is_full():
            print(f"Boat {i} with destination {random.choice(destination)} comes")
            self.boats.enqueue(f"boat{i}")
        else:
            print("Queue for boats is full")
    
    def avg_waiting_pass_time(self):
        return self.boat_interval / 2

    def perfect_interval(self):
        return CAPACITY * self.pass_interval

    def people_dissapers(self, capacity):
        if self.passengers:
            dissapeared = 0
            while dissapeared < capacity:
                self.passengers.dequeue()
                dissapeared += 1
            
            print("people are on board")
    
    def boat_departures(self):
        if self.boats:
            boat = self.boats.dequeue()       
            print(f"{boat} departures")


    def hasBoat(self):
        if self.boats: return True 
        else: return False

    def statistic(self):
        print(f"avg of waiting {self.avg_waiting_pass_time()}")
        print(f"perfect interval {self.perfect_interval()}")

    def simulate(self):
        curr_time = 1

        boats = [
            Boat('Keks', 10, 'other'),
            Boat('Philip', 10, 'end'),
            Boat('Cucumber', 10, 'other'),
            Boat('prosto boat', 10, 'other'),
            Boat('Korablik edet tuda', 10, 'other')
        ]
        pass_i = 1
        boat_i = 1
        while True:
            if curr_time % 6 == 0:
                self.boat_come(boat_i)
                self.people_dissapers(CAPACITY)
                self.boat_departures()
                self.statistic()
                boat_i += 1

            self.pass_come(pass_i)

            pass_i += 1
            
            time.sleep(1)
            curr_time += 1

dock = Dock(30, 5, 5, 1)
dock.simulate()
            
