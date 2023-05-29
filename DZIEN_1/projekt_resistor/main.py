from oldresistor import OldResistor

r0 = OldResistor(10.22E2)
print(f"________ {r0.__class__.__name__} ___________")
print(r0)
print(r0.get_ohms())
r0.set_ohms(5.5E3)
print(r0.get_ohms())
