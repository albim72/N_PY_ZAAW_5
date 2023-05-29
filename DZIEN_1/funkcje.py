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




