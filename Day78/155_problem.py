# Create a class Stack with a list to store items. Add methods push(item), pop() (removes and returns last item), and is_empty() (returns True/False).

class Stack:
    def __init__(self):
        self.stack_items = []

    def pop(self):
        return self.stack_items.pop()

    def push(self, item):
        self.stack_items.append(item)

    def is_empty(self):
        return len(self.stack_items) == 0


s = Stack() 
print(s.is_empty()) 
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.is_empty())