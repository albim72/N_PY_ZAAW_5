class HelloMeta(type):
    def hello(cls):
        print(f"informacja z {type(cls)}, klasa HelloMeta")

    def __call__(self, *args, **kwargs):
        cls = type.__call__(self,*args)
        setattr(cls,"hello",self.hello)
        return cls

class TryHello(object,metaclass=HelloMeta):
    def greet(self):
        self.hello()


gree = TryHello()
gree.greet()
gree.hello()
