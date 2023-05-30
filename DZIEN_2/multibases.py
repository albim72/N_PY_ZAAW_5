class MultiBases(type):
    def __new__(cls,clsname,bases,attrs):
        if len(bases) > 1:
            raise TypeError("możliwe tylko jednodziedziczenie!!!")
        return super().__new__(cls,clsname,bases,attrs)

class Zw:
    pass

class Base(metaclass=MultiBases):
    pass

class A(Base):
    pass

class B(A,Zw):
    pass
