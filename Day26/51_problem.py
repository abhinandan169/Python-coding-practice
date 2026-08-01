# Create a Counter class with a class variable count (shared across all objects, starts at 0). Every time a new object is created, count should increase by 1 (hint: use __init__ to increment it). Add a method show_count() that prints the current count. Create 3 objects and print the count after each.



class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    def show_count(self):
        print(f"Current count: {Counter.count}")



c1 = Counter()
c1.show_count()

c2 = Counter()
c2.show_count()

c3 = Counter()
c3.show_count()