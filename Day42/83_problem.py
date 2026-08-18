# Create a Player class with attributes name, runs, and balls_faced. Add a method strike_rate() that returns (runs / balls_faced) * 100. Create a list of 3 players and print each one's strike rate.

class Player:
    def __init__(self, name, runs, balls_faced):
        self.name = name
        self.runs = runs
        self.balls_faced = balls_faced

    def strike_rate(self):
        return (self.runs / self.balls_faced) * 100

p1 = Player("Abhinandan", 43, 20)
p2 = Player("MS Dhoni", 88, 44)
p3 = Player("Abhishek Bacchan", 15, 6)

players = [p1, p2, p3]

for player in players:
    print(f"{player.name} made {player.runs} runs, strike rate is {player.strike_rate()}")