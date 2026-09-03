# Create a class Contact with attributes name and phone. Create a class ContactBook that stores a list of Contact objects. Add a method find_contact(name) that searches the list and prints the phone number if found, otherwise prints "Not found"


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactBook:
    def __init__(self):
        self.list_contact = []

    def find_contact(self, name):
        for contact in self.list_contact:
            if contact.name == name:
                print(contact.phone)
                return 
        print("Not Found")


cb = ContactBook()
cb.list_contact.append(Contact("Rahul", "9876543210"))
cb.list_contact.append(Contact("Priya", "9123456780"))
cb.find_contact("Priya")
cb.find_contact("Aman")        