from decimal import Decimal

class Akwizytor:
    """
    Pracownik, którego wynagrodzenie opiera się na prowizji od sprzedaży
    Umowa: B2B
    """
    def __init__(self,imie,nazwisko,nr_ubezpieczenia,sprzedaz,prowizja):
        self._imie = imie
        self._nazwisko = nazwisko
        self._nr_ubezpieczenia = nr_ubezpieczenia
        self.sprzedaz = sprzedaz
        self.prowizja = prowizja
        
    def __repr__(self):
        return (f'Akwizytor: {self.imie} {self.nazwisko}' +
                f'numer ubezpieczenia: {self._nr_ubezpieczenia}\n'
                f'sprzedaż: {self.sprzedaz} zł\n'
                f'prowizja: {self.prowizja} procent.')
    
    #property imie   
    @property
    def imie(self):
        return self._imie
    
    @imie.setter
    def imie(self,nimie):
        self._imie = nimie

    #property nazwisko
    @property
    def nazwisko(self):
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, nnazwisko):
        self._nazwisko = nnazwisko

    #property nr_ubezpieczenia
    @property
    def nr_ubezpieczenia(self):
        return self._nr_ubezpieczenia

    @nr_ubezpieczenia.setter
    def nr_ubezpieczenia(self, nnr_ubezpieczenia):
        self._nr_ubezpieczenia = nnr_ubezpieczenia
        
    #property sprzedaz
    @property
    def sprzedaz(self):
        return self._sprzedaz

    @sprzedaz.setter
    def sprzedaz(self, kwota):
        if kwota < Decimal('0.00'):
            raise ValueError('Wartość sprzedaży nie może być ujmena!')
        self._sprzedaz = kwota
    
    #property prowizja
    @property
    def prowizja(self):
        return self._prowizja

    @prowizja.setter
    def prowizja(self, procent):
        if not (Decimal('0.0')<procent<=Decimal('30.00')):
            raise ValueError('Prowizja musi zawierać się w przedziale powyżej 0 do 30 procent')
        self._prowizja = procent
        
    def zarobek(self):
        return self.sprzedaz*(self.prowizja/Decimal('100.0'))
        
        
        
        
