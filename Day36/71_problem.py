# Create a Weather class with attribute temp_celsius. Add a method is_hot() that returns True if temperature is above 35°C, else False. Create a list of 4 Weather objects with different temperatures. Loop through and print which ones are "hot".



class Weather:
    def __init__(self, temp_celsius):
        self.temp_celsius = temp_celsius

    def is_hot(self):
        if self.temp_celsius > 35:
            return True
        else:
            return False

w1 = Weather(35)
w2 = Weather(40)
w3 = Weather(20)
w4 = Weather(25)

weathers = [w1, w2, w3, w4]

for w in weathers:
    if w.is_hot():
        print(f"{w.temp_celsius}°C is Hot")