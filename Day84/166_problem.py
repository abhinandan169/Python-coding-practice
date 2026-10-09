# Create a class MathUtils with two static methods: is_even(n) returns True if n is even, and cube(n) returns the cube of n. Call both without creating an object.


class MathUtils:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def cube(n):
        return n * n * n

print(MathUtils.is_even(8))
print(MathUtils.cube(3))      