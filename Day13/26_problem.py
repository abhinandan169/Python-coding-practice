# Create a Queue class (using a list internally) with two methods — enqueue(item) that adds an item to the end, and dequeue() that removes and returns the item from the front. If the queue is empty, dequeue() should print "Queue is empty" instead of throwing an error.



class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            print("Queue is Empty")
        else:
            return self.items.pop(0)

q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
     
