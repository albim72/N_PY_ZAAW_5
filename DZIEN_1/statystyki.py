liczby = [56,-900,34,56,789,0,112,-114,198,-78,3,1,677,-344,-3,2]

def policz_statystyki(lista):
    minimum = min(lista)
    maksimum = max(lista)
    rozstep = maksimum-minimum
    liczbael = len(lista)
    sumael = sum(lista)
    sredart = sumael/liczbael
    return minimum,maksimum,rozstep,liczbael,sumael,sredart

wynik = policz_statystyki(liczby)
print(wynik)
print(type(wynik))

mini,maxi,roz,el,sm,art = policz_statystyki(liczby)
print(f"wartość maksymalna: {maxi}, wartość minimalna: {mini}, rozstęp: {roz},"
      f" liczba elementów:{el}, suma elementów: {sm}, średnia arytmetyzna: {art:.2f}")
