#A SIMPLE OOP PYTHON ASSIGNMENT...
class Item:
    def __init__(self,name: str,price: float , quantity=0):
        #RUN VALIDATIONS TO THE RECEIVED ARGUEMENTS.
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greate thanm or equal to zero!"
        
        #ASSIGN TO SELF OBJECT
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Reveries",1000,100000)
item2 = Item("phone",50000,3)
