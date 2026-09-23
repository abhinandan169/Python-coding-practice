# Create a class Cylinder with attributes radius and height. Add methods volume() (formula: 3.14 * radius * radius * height) and surface_area() (formula: 2 * 3.14 * radius * (radius + height)).


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return 3.14 * self.radius * self.radius * self.height

    def surface_area(self):
        return 2 * 3.14 * self.radius * (self.radius + self.height)


c1 = Cylinder(4, 10)
print(c1.volume())

c2 = Cylinder(6, 8)
print(c2.surface_area())