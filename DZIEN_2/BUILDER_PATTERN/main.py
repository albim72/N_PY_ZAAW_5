from director import Director
from concretebuilder import ConcreteBuilder1

director = Director()
builder = ConcreteBuilder1()
director.builder = builder

print("produkt pdostawowy: ")
director.build_minimal_version()
builder.product.list_parts()

print("\n")

print("produkt pełny: ")
director.build_maximal_version()
builder.product.list_parts()


print("\n")

print("Podukt - -własna wersja: ")
builder.produce_part_a()
builder.produce_part_c()
builder.product.list_parts()
