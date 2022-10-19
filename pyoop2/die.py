#CLASS NAMED DIE...
import random
class Die:
    def __init__(self):
        self.sides = 6
    def roll_die(self):
        roll = random.randint(1,6)
        print(roll)



ad = Die()
ab = ad.sides
print(ab)
ad.roll_die()