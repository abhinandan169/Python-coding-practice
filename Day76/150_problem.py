# Create a class Musician with method play_music() printing "Playing music". Create a class Athlete with method play_sport() printing "Playing sport". Create a class Student that inherits from both, and call both methods on a Student object.

class Musician:
    def play_music(self):
        print("Playing music")

class Athlete:
    def play_sport(self):
        print("Playing sport")

class Student(Musician, Athlete):
    pass 

s = Student()
s.play_music()
s.play_sport()