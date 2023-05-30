from decimal import Decimal
from akwizytor import Akwizytor

class AkwizytorNaEtacie(Akwizytor):
    """
    Pracownik, którego wynagrodzenie opiera się na prowizji od sprzedaży oraz stałej pensji
    Umowy: o pracę i zlecenie
    """

    def __init__(self, imie, nazwisko, nr_ubezpieczenia, sprzedaz, prowizja, pensja):
        super().__init__(imie, nazwisko, nr_ubezpieczenia, sprzedaz, prowizja)
        self.pensja = pensja

    def __repr__(self):
        return 'Etatowy ' + super().__repr__() + \
            f'\npensja: {self.pensja:.2f} zł'

    @property
    def pensja(self):
        return self._pensja

    @pensja.setter
    def pensja(self,kwota):
        if kwota < Decimal("1000.00"):
            raise ValueError('Wynagordzenie nie może być mniejsze niż 1000 zł')
        self._pensja = kwota

    def zarobek(self):
        return super().zarobek() + self.pensja



