#tworzenie słownika opartego na definicji kluczy i wartości za pomocą tylko list i krotek
#natomiast wartości mogą posiadać tylko typ: int i float

class IntFloatValueError(Exception):
    def __init__(self,value):
        self.value = value
        
    def __str__(self):
        return f'{self.value} jest niewłaściwe. Klasa akceptuje jedynie wartości int i float! '
    
class KeyValueConstructError(Exception):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        
    def __str__(self):
        return f'klucze i wartości mogą być wprowadzone jedynie za pomocą list lub krotek\n' \
               f'{self.key} jest typu: {type(self.key)}\n' \
               f'{self.value} jest typu: {type(self.value)}'
    

class 
