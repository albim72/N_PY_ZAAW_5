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

class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print('adding the tomato sauce to your margarita...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the tomato sauce...')

    def add_topping(self):
        topping_desc ='double mozarella, oregano'
        topping_items = (PizzaTopping.double_mozarella,PizzaTopping.oregano)
        print(f'adding the topping ({topping_desc}) to your margarita...')
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'dane with the topping ({topping_desc})')

    def bake(self):
        self.progress = PizzaProgress.baking
        print(f'baking your margarita for {self.baking_time} s')
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('Your margarita is ready!!!')
        
        
        
class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        print('adding the creme fraiche sauce to your creamy bacon...')
        self.pizza.sauce = PizzaSauce.cream_fraiche
        time.sleep(STEP_DELAY)
        print('done with the creme fraiche sauce...')

    def add_topping(self):
        topping_desc ='mozarella, bacon, ham, mushrooms, red onion, oregano'
        topping_items = (PizzaTopping.mozarella,
                         PizzaTopping.bacon,
                         PizzaTopping.ham,
                         PizzaTopping.mushrooms,
                         PizzaTopping.red_onion,
                         PizzaTopping.oregano)
        print(f'adding the topping ({topping_desc}) to your creamy bacon...')
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'done with the topping ({topping_desc})')

    def bake(self):
        self.progress = PizzaProgress.baking
        print(f'baking your creamy bacon for {self.baking_time} s')
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('Your creamy bacon is ready!!!')
