from decimal import Decimal
from akwizytor import Akwizytor
from akwizytornaetacie import AkwizytorNaEtacie


class Firma:
    def __repr__(self):
        return 'Właściciel firmy otrzymuje stałe roczne wynagrodzenie, w oparciu o wyniki finansowe firmy'
    def zarobek(self):
        return Decimal('12_000_000')

boss = Firma()
akw = Akwizytor('Anna','Kos',523545,Decimal('324500'),Decimal('7.8'))
akwna = AkwizytorNaEtacie('Emil','Krupa',13231321,Decimal('567334'),Decimal('5.2'),Decimal('4_500.0'))

prac = [akw,akwna,boss]
for p in prac:
    print(p)
    print(f'{p.zarobek():,.2f} zł \n')
