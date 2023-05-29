from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance

r0 = OldResistor(10.22E2)
print(f"________ {r0.__class__.__name__} ___________")
print(r0)
print(r0.get_ohms())
r0.set_ohms(5.5E3)
print(r0.get_ohms())

r1 = Resistor(5.1E3)
print(f"________ {r1.__class__.__name__} ___________")
print(r1.ohms)
r1.ohms = 4.5E2
print(r1.ohms)

print(f'układ elektryczny:\noporność: {r1.ohms} om\nnapięcie prądu: {r1.voltage} V\n'
      f'natężenie prądu: {r1.current} A')

r2 = VoltageResistance(1.1E3)
print(f"________ {r2.__class__.__name__} ___________")
print(f'natężenie początkowe prądu: {r2.current} A')
r2.voltage = 55
print(f'napięcie końcowe prądu: {r2.voltage} V')
print(f'natężenie końcowe prądu: {r2.current} A')
