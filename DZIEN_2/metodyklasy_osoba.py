from datetime import date

class Osoba:
    def __init__(self,imie,wiek):
        self.imie = imie
        self.wiek = wiek

    #metoda klasy
    @classmethod
    def ile_od_narodzin(cls,imie,rok):
        return cls(imie,date.today().year - rok)

    #metoda statyczna
    @staticmethod
    def czydorosly(wiek):
        return wiek>=18


pr1 = Osoba("Roman",45)
pr2 = Osoba.ile_od_narodzin("Anna",1981)

print(pr1.wiek)
print(pr2.wiek)
print(type(pr1))
print(type(pr2))

print(Osoba.czydorosly(101))
print(pr1.czydorosly(pr1.wiek))
