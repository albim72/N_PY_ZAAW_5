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
