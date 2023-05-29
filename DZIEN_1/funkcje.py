#przykład 1
def multi(n:int)->int:
    return lambda a:a*n

print(multi(7)(9))

#funkcja wyższego rzędu -> funkcja której mninium jedny z argumentów jest funkcja

num = [45,8,9,112,-45,22,66,8,-4,9,11,196,555]
#stwórz listę parz i wprowadź do niej wszystkie wartości parzyste z listy num
parz = list(filter(lambda x:x%2==0,num))
print(parz)

#stwórz listę cube i wprowadx do niej wszystkie wartości z num podniesione do potęgi 3
cube = list(map(lambda x:x**3,num))
print(cube)

def policz(x):
    return (x+5)**4

nbp = list(map(policz,num))
print(nbp)


#przykład 2
def witaj(imie):
    return f"Miło Cię widzieć {imie}!"

def konkurs(imie,punkty):
    return f"uczestnik konkursu {imie}, liczba punktów: {punkty}"

def student(imie,kierunek,wiek):
    return f"Student {imie}, wiek: {wiek}, kierunek: {kierunek}"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Anna",56))
print(osoba(student,"Nadia",23,"Informatyka"))

#przykład3

def rejestracja(oplata):
    def lista():
        return "Opłata wniesiona, jesteś na liście zawodników."
    def brak():
        return "Brak wpłaty. Zapłać w ciągu 5 dni!"
    def error():
        return "Błąd płatności. Powtórz."

    if oplata == 1:
        return lista
    elif oplata == 0:
        return brak
    else:
        return error


print(rejestracja(0)())
print(rejestracja(1)())
print(rejestracja(13)())

#przykład4

def startstop(funkcja):
    def wrapper(*args):
        print("startowanie procesu...")
        funkcja(*args)
        print("kończenie procesu...")
    return wrapper


def zawijanie(czego):
    print(f"zawijanie {czego} w sreberka...")

print("_"*30)
zw = startstop(zawijanie)
zw("czekoladek")

@startstop
def dmuchanie(czego):
    print(f"dmuchanie {czego} w urodziny")


dmuchanie("świeczek na torcie")

@startstop
def f(x):
    print(f"wynik = {x*100-32}")

f(99)
