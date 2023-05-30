from czlonekrodu import CzlonekRodu

class Tywin(CzlonekRodu):
    def walka(self):
        if self.punkty_walki>self.punkty_palacowe and self.punkty_walki > 6:
            print(f"{self.tytul} {self.__class__.__name__} wysłany na pole walki")
        else:
            print(f"{self.tytul} {self.__class__.__name__} pozostaje w pałacu")

    def negocjacja(self):
        if self.punkty_walki < self.punkty_palacowe and self.punkty_palacowe > 6:
            print(f"{self.tytul} {self.__class__.__name__} wysłany do negocjacji")
        else:
            print(f"{self.tytul} {self.__class__.__name__} wysłany na pole walki")

    def uczta(self):
        pass
