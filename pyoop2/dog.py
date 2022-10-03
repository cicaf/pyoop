#A CLASS NAMED DOG WITH SMALL MODULES...
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} sit boy...")

    def roll_over(self):
        print(f"{self.name} roll over boi!")


pluto = Dog('Pluto',12)
pluto.sit()
pluto.roll_over()
