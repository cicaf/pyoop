#A SIMPLE CAR CLASS...
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.year = year
        self.model = model
        self.odometer = 23
    def describe(self):
        the_car = f" the car is a {self.make.title()} {self.model} made in {self.year} with {self.odometer}km milage , get it!"
        return the_car

    def odometer_update (self,mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("we cannt roll back the safaris dude...")

    def increment_odometer(self,miles):
        self.odometer += miles
class Electrical_Car(Car):

    """REPRESENTS ASPECTS OF A CAR SPECIFIC TO ELECTRICAL VEHICLES"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)






toyo = Car("toyota landcruiser",'LC 300 ',2024)
toyo.odometer_update(47)
toyo.name = "BMW"
ans = toyo.describe()
print(ans)