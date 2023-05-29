class Testowa(object):
    # def  __new__(cls, *args, **kwargs):
    #     return object.__new__(Testowa)

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __call__(self, *args, **kwargs):
        return f"iloczyn a*b = {self.a*self.b}"

    def __repr__(self):
        return f"wartości -> a = {self.a}, b = {self.b}!"

t = Testowa(4,7)
print(t)
print(t())
