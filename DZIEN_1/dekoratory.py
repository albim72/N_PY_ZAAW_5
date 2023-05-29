import time
#przykład1
def pomiarczasu(funkcja):
    def wrapper(*args):
        starttime = time.perf_counter()
        funkcja(*args)
        endtime = time.perf_counter()
        print(f"czas wykonania funckji: {endtime-starttime} s")
    return wrapper

def sleep(funkcja):
    def wrapper(*args):
        time.sleep(2)
        return funkcja(*args)
    return wrapper


@sleep
@pomiarczasu
def big_lista(n):
    sum([(i+1)**2 for i in range(n)]) #list comprehension

big_lista(13_000_000)

#przykład2

def debug(funkcja):
    def wrapper(*args):
        print(f'wołana funkcja to: {funkcja.__name__}')
        funkcja(*args)
    return wrapper

@debug
def info(msg):
    print(f'ważna informacja: {msg}')

info("takie tam")
