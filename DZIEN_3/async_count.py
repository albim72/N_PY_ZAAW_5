import asyncio
import time

async def count():
    print("początek....")
    await asyncio.sleep(1)
    print("koniec....")

async def main():
    await asyncio.gather(count(),count(),count(),count(),count())

if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} jest wykonywany w {elapsed:.2f} s")
