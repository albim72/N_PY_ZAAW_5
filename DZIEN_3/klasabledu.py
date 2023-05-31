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


class CustomIntFloatDict(dict):
    
    empty_dict={}
    
    def __init__(self,key=None,value=None):
        if key is None or value is None:
            self.get_dict()
        elif not isinstance(key,(tuple,list,)) or not isinstance(value,(tuple,list,)):
            raise KeyValueConstructError(key,value)
        else:
            zipped = zip(key,value)
            for k,val in zipped:
                if not isinstance(val,(int,float)):
                    raise IntFloatValueError(val)
                dict.__setitem__(self,k,val)
            
    def get_dict(self):
        return self.empty_dict
    
    
    def __setitem__(self, key, value):
        if not isinstance(value, (int, float)):
            raise IntFloatValueError(value)
        return dict.__setitem__(self, key, value)
    
    
