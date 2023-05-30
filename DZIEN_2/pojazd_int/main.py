from pojazd import Pojazd

p = Pojazd()
odl = float(input("Podaj odległość w km: "))
lt = float(input("Podaj liczbę spalonych litrów: "))
cn = float(input("Podaj cenę za litr paliwa...."))

print(f"spalanie [l/100km]: {p.spal_100(odl,lt):.2f}")
print(f"koszty przejazdu na trasie {odl} km wynoszą {p.kosztyprzejazdu(odl,lt,cn):.2f} zł")
