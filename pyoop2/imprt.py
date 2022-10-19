#TRYING TO IMPORT FROM CAR CLASS...
from herit import Car, Battery ,ElectricCar

mycar = ElectricCar("Tesla","Cybertruck","2022")
mycar.read_odometer()
print(mycar.get_desc_name())
mycar.fill_gas()
mycar.battery_size.desc_batt()
mycar.battery_size.range()