###WHEN AN INSTANCE TAKES THE ATTRIBUTE OF A CLASS....THE ORIGINAL IS THE PARENT WHEREAS THE 
#ONE TAKING THE ATTRIBUTE IS THE CHILD CLASS...
#WE USE THE __init___ METHOD FOR ALL THESE...
#example,we can model an electric car from all these...



class Car:
    def __init__(self,model,make,year):
        self.model = model
        self.make = make
        self.year = year
        self.odometer_reading = 0

    def get_desc_name(self):
        name = f"The car is a {self.model} uhmmm {self.make} ya {self.year}  "
        return name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} mileage")

    def update_odometer(self,new):
        new = input("Please sema your odometer reading :")
        if new >= self.odometer_reading:
            self.odometer_reading = new
        else:
            print("The odometer cannt be back tracked...")

    def incr_odometer(self,travel_dist):
        self.odometer_reading += travel_dist
        updated = f"new mileage is {self.odometer_reading} after addition"
        return updated

    def fill_gas(self):
        print(f"lets go to a gas station")
##HERE WE SEE SOME SERIOUS INHERITANCE IN ACTION..
class ElectricCar(Car):
    def __init__(self, model, make, year):
        super().__init__(model, make, year)

        self.battery_size = Battery()

    
    #METHOD OVERRIDE
    def fill_gas(self):
        print("we dont need gas....we electric bruh")

    
class Battery:
    #MODELING A DEEP CYCLE LITHIUM ION CELL FOR OUR ELECTRIC VEHICLES.
    def __init__(self,batt_size = 75):
        #INITIALIZE THE BATTERY ATTRIBUTES...
        self.batt_size = batt_size

    def desc_batt(self):
        #METHOD TO DESCRIBE OUR BATTERY...
        print(f"the size of the battery is {self.batt_size} kilowatthour")

    def range(self):
        if self.batt_size == 75:
            range = 260
        elif self.batt_size ==100:
            range = 315
        print(f"The range of the Tesla is {range} miles when full")



