class MojaMeta(type):
    def __new__(cls,clsname,bases,attrsdict):
        print(f"nazwa klasy: {clsname}")
        print(f"klasy dziedziczone: {bases}")
        print(f"zbiór atrybutów: {attrsdict}")
        print(cls.info(cls))
        return type.__new__(cls,clsname,bases,attrsdict)

    def info(cls):
        return "metaklasa działa...."



class Zwykla:
    def oblicz(self,x,y):
        return 2*x-y

class Pierwsza(Zwykla,metaclass=MojaMeta):

    def oblicz(self, x, y):
        return super().oblicz(x, y) - 4.5

class Druga(Pierwsza):
    pass

class Dodatkowa:
    pass

class Trzecia(Dodatkowa,Druga):
    pass
