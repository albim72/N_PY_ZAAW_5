from tywin import Tywin
from tyrion import Tyrion

tw = Tywin("Lannister","Lord","m",7,7,9)
tr = Tyrion("Lannister","Lord","m",5,9,10)

print("_________ Lord Tywin ___________")
tw.walka()
tw.negocjacja()
tw.uczta()
print("_________ Lord Tyrion ___________")
tr.walka()
tr.negocjacja()
tr.uczta()
