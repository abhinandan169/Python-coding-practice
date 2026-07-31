# Create a Person class with a private attribute __age (using double underscore). Add a method set_age(age) to set the age (but only if age > 0, otherwise print "Invalid age"), and a method get_age() that returns the age. Create an object, try setting a valid age and an invalid age, then print it.


class Person:
    def __init__(self, age):
        self.__age = age

    def set_age(self, age):
        if age > 0:
            self.__age = age
            print("valid age")
        else:
            print("Invalid age")    

    def get_age(self):
        return self.__age


p = Person(18)

p.set_age(20)
print(p.get_age())

p.set_age(-5)
print(p.get_age()) 


