# Create a class Address with attributes city and pincode. Create a class Person with attributes name and an Address object. Add a method show_details() in Person that prints the name, city, and pincode.

class Address:
    def __init__(self, city, pincode):
        self.city = city
        self.pincode = pincode

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address 

    def show_details(self):
        print(f"My name is {self.name}. I am from {self.address.city} and area pincode is {self.address.pincode}")


a = Address("Uttar Pradesh", "110001")
p = Person("Abhinandan", a)
p.show_details()                 