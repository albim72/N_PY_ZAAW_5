from czlonekrodu import CzlonekRodu

class Tyrion(CzlonekRodu):
    def walka(self):
        if self.punkty_walki>self.punkty_palacowe and self.punkty_walki > 7:
            print(f"{self.tytul} {self.__class__.__name__} wysłany na pole walki")
        else:
            print(f"{self.tytul} {self.__class__.__name__} pozostaje w pałacu")

    def negocjacja(self):
        if self.punkty_palacowe >= 8:
            print(f"{self.tytul} {self.__class__.__name__} wysłany do negocjacji")
        else:
            print(f"{self.tytul} {self.__class__.__name__} wysłany na pole walki")

    def uczta(self):
        if self.punkty_palacowe >= 7 and self.doswiadczenie >= 7: 
            print(f"{self.tytul} {self.__class__.__name__} jedzie na ucztę")
        else:
            print(f"{self.tytul} {self.__class__.__name__} pozostaje w pałacu")
