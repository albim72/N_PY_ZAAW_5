from typing import List,Protocol

class Item(Protocol):
    quantity:float
    price:float

class Product:
    def __init__(self,name:str,quantity:float,price:float):
        self.name = name
        self.quantity = quantity
        self.price = price

def calulate_total(items:List[Item]) -> float:
    return sum(item.quantity*item.price for item in items)

total = calulate_total([
    Product('A',6,171),
    Product('B',1,56.4),
    Product('C',3,79.5),
    Product('AD',2,211)
])

print(f"do zapłaty {total} zł")



