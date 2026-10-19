# Using Q182's classes, create Child2(Mother, Father) (order ulta kar do) and call skills() again. Then print Child2.mro() for both child classes.



class Father:
    def skills(self):
        print("Driving")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()  

class Child2(Mother, Father):
    pass

c2 = Child2()
c2.skills()          

print(Child.mro())
print(Child2.mro())