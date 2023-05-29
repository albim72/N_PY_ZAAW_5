#funkcje parsujące listę i słownik
def czytaj_liste(lista):
    for i,j in enumerate(lista):
        print(f"Element listy o indeksie: {i+1}, posiada wartość: {j}")
        
def czytaj_slownik(slownik):
    for x,y in slownik.item():
        print(f"pole słownika o kluczu {x} posiada wartość: {y}")
