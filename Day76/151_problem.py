# Create a class Fraction with attributes numerator and denominator. Add a method simplify() that reduces the fraction to its simplest form using the GCD (hint: use math.gcd(a, b)).

import math


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // gcd
        self.denominator = self.denominator // gcd
        print(f"{self.numerator}/{self.denominator}")

f = Fraction(8, 12)
f.simplify()        