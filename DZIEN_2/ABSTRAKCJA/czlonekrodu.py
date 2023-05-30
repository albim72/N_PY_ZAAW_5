from abc import ABC,abstractmethod

class CzlonekRodu(ABC):
    def __init__(self,nazwarodu,tytul,plec,punkty_walki,punkty_palacowe,doswiadczenie):
        self.nazwarodu = nazwarodu
        self.tytul = tytul
        self.plec = plec
        self.punkty_walki = punkty_walki
        self.punkty_palacowe = punkty_palacowe
        self.doswiadczenie = doswiadczenie
        self.create_hero()

    def create_hero(self):
        print(f"Utworzono nową postać -> członek rodu: {self.nazwarodu}")

    @abstractmethod
    def walka(self):
        pass

    @abstractmethod
    def negocjacja(self):
        pass

    @abstractmethod
    def uczta(self):
        pass
