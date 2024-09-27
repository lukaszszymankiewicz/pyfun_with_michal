# this is a function
def zrob_zielone(a: str):
    counter = 0
    return "zielony " + a

# class
class Kolorator:
    ###
    def __init__(self, counter: int):
        self.counter = counter
        self.duppa = "blada"
    ###

    def zrob_zielone(self, a: str):
        self.counter += 1
        return "zielony " + a

    def zrob_czerowy(self, a: str):
        self.counter += 1
        return "czerowy " + a

# k is an instance of the class Kolorator
k = Kolorator(10)