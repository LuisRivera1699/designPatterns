from __future__ import annotations
from abc import ABC, abstractmethod


#### --- Declaracion de las clases abstractas pricipales --- ###

# Declaracion de las clases Abstract Product que crean las
# interfaces para cada tipo de Concrete Product.

class AbstractProduct_Boton(ABC):
    @abstractmethod
    def dibujar(self):
        pass

class AbstractProduct_CajaTexto(ABC):
    @abstractmethod
    def dibujar(self):
        pass

# Declaracion de la clase Abstract Factory que crea la
# interface que creara los objetos Abstract Product

class AbstractFactory_GUI(ABC):
    @abstractmethod
    def crearBoton(self) -> AbstractProduct_Boton:
        pass

    @abstractmethod
    def crearCajaTexto(self) -> AbstractProduct_CajaTexto:
        pass


### --- Declaracion de las clases concretas principales --- ###

# Declaracion de las clases Concrete Factory que implementaran los
# metodos abstractos de su clase padre Abstract Factory para crear
# los Concrete Products

class ConcreteFactory_MacOS(AbstractFactory_GUI):
    def crearBoton(self) -> AbstractProduct_Boton:
        return ConcreteProduct_Boton_MacOS()
    
    def crearCajaTexto(self) -> AbstractProduct_CajaTexto:
        return ConcreteProduct_CajaTexto_MacOS()

class ConcreteFactory_Windows(AbstractFactory_GUI):
    def crearBoton(self) -> AbstractProduct_Boton:
        return ConcreteProduct_Boton_Windows()

    def crearCajaTexto(self) -> AbstractProduct_CajaTexto:
        return ConcreteProduct_CajaTexto_Windows()

# Declaracion de las clases Concrete Product, que implementaran los metodos
# abstractos de su clase padre Abstract Product respectiva

class ConcreteProduct_Boton_Windows(AbstractProduct_Boton):
    def dibujar(self):
        print('Se ha dibujado un boton en Windows')

class ConcreteProduct_CajaTexto_Windows(AbstractProduct_CajaTexto):
    def dibujar(self):
        print('Se ha dibujado una caja texto en Windows')

class ConcreteProduct_Boton_MacOS(AbstractProduct_Boton):
    def dibujar(self):
        print('Se ha dibujado un boton en MacOS')

class ConcreteProduct_CajaTexto_MacOS(AbstractProduct_CajaTexto):
    def dibujar(self):
        print('Se ha dibujado una caja texto en MacOS')


### --- Declaracion de la clase Cliente --- ###

# Usa las clases hijas de las clases Abstract Product y Abstract Factory

class Client():

    def __init__(self, factory : AbstractFactory_GUI):
        self.boton = factory.crearBoton()
        self.cajaTexto = factory.crearBoton()

    def dibujar(self):
        self.boton.dibujar()
        self.cajaTexto.dibujar()


### --- Prueba --- ###

def main():
    pass

if __name__ == "__main__":
    windows_factory = ConcreteFactory_Windows()
    macOS_factory = ConcreteFactory_MacOS()
    client = Client(windows_factory)
    client_two = Client(macOS_factory)

    print("App: Launched with the Concrete Factory Windows.")
    client.dibujar()
    print("\n")

    print("App: Launched with the Concrete Factory MacOS.")
    client_two.dibujar()