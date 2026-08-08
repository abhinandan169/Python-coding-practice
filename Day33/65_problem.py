# Create a class Countdown that takes a start number. Implement __iter__(self) (returns self) and __next__(self) (returns the next number counting down to 0, and raises StopIteration when done). Use it in a for loop to print the countdown.




class Countdown:
    def __init__(self, start):
        self.current = start    

    def __iter__(self):
        return self             
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration   
        else:
            num = self.current    
            self.current -= 1     
            return num

c = Countdown(3)
for num in c:
    print(num)        
