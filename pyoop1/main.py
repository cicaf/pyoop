#A SIMPLE OOP PYTHON ASSIGNMENT...
class Item:
    def __init__(self,name ,price , quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

book = Item("Reveries",1000,100000)
item2 = Item("phone",50000,3)

print(book.name)
print(item2.quantity)
