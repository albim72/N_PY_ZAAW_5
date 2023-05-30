odp = input("Czy Ziemia jest płaska? Chcesz znać odpowiedź?(t/n): ")
if odp.lower() == 't':
    required = True
else:
    required = False


def odpowiedz(self,*args):
    return "tak! Ziemia jest płaska!"

def odpowiedz_new(self,*args):
    return "nie! Ziemia jest elipsoidą!"

def brak(self,*args):
    return "brak odpowiedzi..."

class SednoOdpowiedzi(type):
    def __init__(cls,clsname,bases,attrs):
        if required:
            if attrs.get('nw') == True:
                cls.odpowiedz = odpowiedz_new
            else:
                cls.odpowiedz = odpowiedz
        else:
            cls.odpowiedz = brak

class Arystoteles(metaclass=SednoOdpowiedzi):
    pass

class Platon(metaclass=SednoOdpowiedzi):
    pass

class SwTomasz(metaclass=SednoOdpowiedzi):
    pass

class Kopernik(metaclass=SednoOdpowiedzi):
    nw = True

class Einstein(metaclass=SednoOdpowiedzi):
    nw = True

class Tales(metaclass=SednoOdpowiedzi):
    pass

fil1 = Arystoteles()
fil2 = Platon()
fil3 = SwTomasz()
fil4 = Kopernik()
fil5 = Einstein()
fil6 = Tales()

print(f'filozof {fil1.__class__.__name__} odpowiada: {fil1.odpowiedz()}')
print(f'filozof {fil2.__class__.__name__} odpowiada: {fil2.odpowiedz()}')
print(f'filozof {fil3.__class__.__name__} odpowiada: {fil3.odpowiedz()}')
print(f'filozof {fil4.__class__.__name__} odpowiada: {fil4.odpowiedz()}')
print(f'filozof {fil5.__class__.__name__} odpowiada: {fil5.odpowiedz()}')
print(f'filozof {fil6.__class__.__name__} odpowiada: {fil6.odpowiedz()}')
