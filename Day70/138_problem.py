# Create two unrelated classes Printer and FaxMachine (no inheritance between them), each with a method operate() that prints what they do. Write a function use_device(device) that calls device.operate(). Call this function with objects of both classes.

class Printer:
    def operate(self):
        print("printing documents")

class FaxMachine:
    def operate(self):
        print("Sending Fax")

def use_device(device):
    device.operate()

use_device(Printer()) 
use_device(FaxMachine())                  