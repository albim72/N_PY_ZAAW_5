from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Pełna nazwa metody: {func.__qualname__}")
        return func(*args,**kwargs)
    return wrapper

def debugmethods(cls):
    for key,val in vars(cls).items():
        if callable(val):
            setattr(cls,key,debug(val))
    return cls


class DebugMeta(type):
    def __new__(cls, clsname, bases, attrs):
        obj = super().__new__(cls, clsname, bases, attrs)
        obj = debugmethods(obj)
        return obj

class Base(metaclass=DebugMeta):pass

class Calculate(Base):
    def add(self,x,y):
        return x+y
    def addict(self,x,y):
        return x-y

class SecondCalc(Calculate):
    def multi(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y


mc = Calculate()
sc = SecondCalc()

print(mc.add(2,5))
print(mc.addict(2,5))
print(sc.multi(2,5))
print(sc.div(2,5))



