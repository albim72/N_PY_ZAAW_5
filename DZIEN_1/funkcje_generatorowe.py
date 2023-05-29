#przykład 1

def liczby():
    for i in range(18):
        yield i*2

for p in liczby():
    print(p)

print(type(liczby()))

#przykład 2

def wznowienie(n,k):
    print("wstrzymanie działania...A")
    yield 1145
    print("wznowienie działania...B")

    print("wstrzymanie działania...B")
    yield n+k
    print("wznowienie działania...C")

    print("wstrzymanie działania...C")
    yield n-k
    print("wznowienie działania...D")

    print("wstrzymanie działania...D")
    yield n*k
    print("wznowienie działania...E")

    print("wstrzymanie działania...E")
    yield n/k
    print("wznowienie działania...F")

for i in wznowienie(6,2):
    if i==1145:
        continue
    print(f"wartość z generatora: {i}")
    

