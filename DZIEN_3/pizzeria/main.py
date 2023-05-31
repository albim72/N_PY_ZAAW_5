from enum import Enum
import time

#faza produkcji pizzy
PizzaProgress = Enum('PizzaProgress','queued preparation baking ready')
#rodzaje ciasta
PizzaDough = Enum('PizzaDough','thin thick')
#sosy
PizzaSauce = Enum('PizzaSauce','tomato creme_fraiche')
#składniki
PizzaTopping = Enum('PizzaTopping','mozarella double_mozarella bacon ham mushrooms red_onion oregano')

#podstawowy czas oczekiwanie na wykonanie czynności
STEP_DELAY = 3

class Pizza:
    def __init__(self,name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []
        
    def __str__(self):
        return self.name
    
    def prepare_dough(self,dough):
        self.dough = dough
        print(f'preparing the {self.dough.name} dough of your {self} ... ')
        time.sleep(STEP_DELAY)
        print(f'done with the {self.dough.name} dough')
    
    
        
