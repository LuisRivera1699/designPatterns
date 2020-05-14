from __future__ import annotations
from abc import ABC, abstractmethod

# Movil interface

class Movil(ABC):
    
    @abstractmethod
    def modelo(self):
        pass

    @abstractmethod
    def precio(self):
        pass

# Servers

class Galaxy(Movil):

    def modelo(self):
        print("Un modelo de Galaxy")

    def precio(self):
        print("El precio de Galaxy")

class iPhone(Movil):

    def modelo(self):
        print("Un modelo de iPhone")

    def precio(self):
        print("El precio de iPhone")

# Movil Facade

class MovilFacade():
    galaxy = Galaxy()
    iphone = iPhone()

    def venderGalaxy(self):
        self.galaxy.modelo()
        self.galaxy.precio()

    def venderiPhone(self):
        self.iphone.modelo()
        self.iphone.precio()


class Cliente():
    movilFacade = MovilFacade()

    def compraGalaxy(self):
        print("Pregunta por: Galaxy ")
        self.movilFacade.venderGalaxy()

    def compraiPhone(self):
        print("Pregunta por: iPhone ")
        self.movilFacade.venderiPhone()


### Test

c = Cliente()

c.compraGalaxy()
c.compraiPhone()