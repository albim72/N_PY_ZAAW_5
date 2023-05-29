import time
#przykład1
def pomiarczasu(funkcja):
    def wrapper():
        starttime = time.perf_counter()
        funkcja()
        endtime = time.perf_counter()
        print(f"czas wykonania funckji: {endtime-starttime} s")
    return wrapper

@pomiarczasu
def big_lista():
    sum([(i+1)**2 for i in range(10_000_000)]) #list comprehension

big_lista()
