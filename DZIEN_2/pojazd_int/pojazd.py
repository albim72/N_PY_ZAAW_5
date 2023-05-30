from ipojazd import IPojzad

class Pojazd(IPojzad):
    def spal_100(self, odl, litry):
        return litry*100/odl

    def kosztyprzejazdu(self, odl, litry, cena_l):
        return self.spal_100(odl,litry)*(odl/100)*cena_l
