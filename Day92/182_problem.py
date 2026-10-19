# Create classes Father and Mother, each with a method skills() printing different text (e.g. "Driving" and "Cooking"). Create a class Child(Father, Mother). Call skills() on a Child object and see which one runs.


class Father:
    def skills(self):
        print("Driving")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()          