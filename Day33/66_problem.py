# Create a Task class with attributes title and done (default False). Create a TodoList class with tasks (empty list). Add methods: add_task(title) (creates a Task and adds it), complete_task(title) (finds task by title and sets done = True), and show_pending() (prints titles of all tasks where done is False).



class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        new_task = Task(title)
        self.tasks.append(new_task)

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.done = True

    def show_pending(self):
        for task in self.tasks:
            if task.done == False:
                print(task.title)



t = TodoList()
t.add_task("Buy groceries")
t.add_task("Finish homework")
t.add_task("Call mom")

t.complete_task("Finish homework")

t.show_pending()


