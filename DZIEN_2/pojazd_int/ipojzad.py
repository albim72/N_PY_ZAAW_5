from abc import ABCMeta, abstractmethod

class IPojzad(metaclass=ABCMeta):
    @abstractmethod
    def spal_100(self,odl,litry):raise NotImplementedError("obowiązkowo zaimplementuj metodę!")
    
    @abstractmethod
    def kosztyprzejazdu(self,odl,litry,cena_l):raise NotImplementedError("obowiązkowo zaimplementuj metodę!")
