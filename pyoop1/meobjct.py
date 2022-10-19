class Car:
    base_price = 10000 ##CLASS VARIABLE
    def __init__(self,windows,doors,power):
        self.windows = windows
        self.doors = doors
        self.power = power

    def what_base_price(self):
        print(f"The base price is {self.base_price} USD ")

    @classmethod

    def inlate_after(cls,inflation):
        cls.base_price = cls.base_price + cls.base_price * inflation/