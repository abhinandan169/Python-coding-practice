# Create a class Pair with attributes a and b. Add __eq__ so that two Pair objects are equal if their a and b values match.

class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

p1 = Pair(4,8)
p2 = Pair(4,8)
print(p1 == p2)       