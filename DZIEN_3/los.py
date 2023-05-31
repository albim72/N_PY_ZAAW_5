import asyncio
import random

#ANSI colors
c= (
    "\033[0m",#kolor domyślny
    "\033[36m",#kolor Cyan
    "\033[91m",#kolor Red
    "\033[35m" #kolor Magenta
)

async def makerandom(idx:int,threshold:int = 6) -> int:
    print(c[idx+1] + f"inicjacja makrandom({idx}).")
    i = random.randint(0,10)
    while i<=threshold:
        print(c[idx + 1] + f"makrandom({idx}) == {i} - wartość zbyt mała. Losuj ponownie....")
        await asyncio.sleep(idx+1)
        i = random.randint(0, 10)
    print(c[idx + 1] + f"--> makrandom({idx}) == {i} zakończone." + c[0])
    return i

async def main():
    res = await asyncio.gather(*(makerandom(i,10-i-1) for i in range(3)))
    return res

if __name__ == '__main__':
    random.seed(444)
    r1,r2,r3 = asyncio.run(main())
    print()
    print(f"rozwiązanie: r1 = {r1}, r2 = {r2}, r3 = {r3}")
