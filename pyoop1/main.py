#A SIMPLE OOP PYTHON ASSIGNMENT...
import csv


class Item:
    # ANOTHER ATTRIBUT...A LIST TO STORE ALL THE INSTANCES...
    all = []

    pay_rate = 0.8 #A CLASS ATRIBUTE FOR 20% DISCOUNT
    def __init__(self,name: str,price: float , quantity=0):
        #RUN VALIDATIONS TO THE RECEIVED ARGUEMENTS.
        #THE ASSERTION STATEMENTS IS USE TO CAPTURE THE ERROR...
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greate thanm or equal to zero!"
        
        #ASSIGN TO SELF OBJECT
        self.name = name
        self.price = price
        self.quantity = quantity

        # To store all the instances we do it like this...
        Item.all.append(self)


    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod    
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        #ITERATE OVER THE LIST
        for item in items:
            Item(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity'))

            )

    
    def __repr__(self):
        return f"Item('{self.name}', {self.price}', {self.quantity})"

"""
    item1 = Item("Phone",1000,100000)
    item2 = Item("Laptop",50000,3)
    item3 = Item("cable",10,1000)
    item4 = Item("mouse",600,3)
    item5 = Item("keyboard",50,5)
    item6 = Item("phone",75,5)
"""
    
Item.instantiate_from_csv()
print(Item.all)

#TO PRINT NAME OF INDIVIDUAL INSTANCES.
