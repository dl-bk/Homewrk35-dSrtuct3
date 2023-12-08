# Розробіть додаток, що імітує чергу запитів до сервера.
# Мають бути клієнти, які надсилають запити на сервер, кожен
# з яких має свій пріоритет. Кожен новий клієнт потрапляє у
# чергу залежно від свого пріоритету. Зберігайте статистику
# запитів (користувач, час) в окремій черзі.
# Передбачте виведення статистики на екран. Вибір необхідних структур даних визначте самостійно.
from datetime import datetime

class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
    def is_empty(self):
        return len(self.queue) == 0
    def is_full(self):
        return len(self.queue) == self.capacity
    def insert_with_priority(self, item, priority):
        if not self.is_full():
            self.queue.append((item, priority))#кортеж (елемент, пріорітет)
            print(f"Елемент {item} з пріорітетом {priority} додано до черги")
            self.queue.sort(key=lambda x: x[1])#сортування за пріорітетом
        else:
            print("Черга заповнена")
    def pull_hignest_priority_element(self):
        if not self.is_empty():
            item, priority = self.queue.pop(0)
            print(f"Елемент {item} з пріорітетом {priority} вилучено з черги")
        else:
            print("Черга порожня")
    def peek(self):
        if not self.is_empty():
            item, priority = self.queue[0]
            print(f"Найбільший за пріорітетом {priority} елемент {item}")
        else:
            print("Черга порожня")
    def show(self):
        if not self.is_empty():
            print("Елементи в черзі")
            for item, priority in self.queue:
                print(f"Елемент {item} з {priority}-пріорітетом")
        else:
            print("Черга порожня")

class Client:
    def __init__(self, name, priority) -> None:
        self.name = name
        self.priority = priority


    def __str__(self) -> str:
        return f"{self.name}"
    
class Request:
    def __init__(self, client) -> None:
        self.client = client
        self.time = datetime.now()

    def __str__(self) -> str:
        return f"{self.client} - {self.time}"


queue = PriorityQueue(5000)

client1 =Client('Boris', 1)
client2 = Client('Arnold', 3)
client3 = Client('Joseph', 7)
client4 = Client('Mahmud', 2)


queue.insert_with_priority(Request(client1), client1.priority)
queue.insert_with_priority(Request(client2), client2.priority)
queue.insert_with_priority(Request(client3), client3.priority)
queue.insert_with_priority(Request(client4), client4.priority)

queue.show()