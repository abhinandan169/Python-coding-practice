# Create a class Queue with a list to store items. Add methods enqueue(item) (add to end), dequeue() (remove and return from front), and is_empty().


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None

        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())
print(queue.dequeue())  
print(queue.is_empty())  