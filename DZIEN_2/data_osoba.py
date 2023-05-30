from dataclasses import dataclass,astuple,asdict,field

@dataclass(order=True)
class Person:
    firstname:str = "Jan"
    lastname:str = "Kot"
    age:int = 40
    job:str = "Data Developer"
    full_name:str = field(init=False,repr=False)
    sort_index:int = field(init=False,repr=False)

    def __repr__(self):
        return f"Pracownik {self.firstname} {self.lastname}, stanowisko: {self.job}"

    def __post_init__(self):
        self.full_name = self.firstname + " " + self.lastname
        self.sort_index = self.age


janek = Person()
print(janek)
print(janek.full_name)

print(astuple(janek))
print(asdict(janek))

janek2 = Person(age=77)

anna = Person("Anna","Kowal",27,"sekretarka")
print(anna)
print(anna.full_name)

print(janek>janek2)
print(janek<janek2)
print(janek == janek2)
