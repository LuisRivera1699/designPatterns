from abc import ABC, abstractmethod

class EuropeanSocketInterface(ABC):
    
    @abstractmethod
    def voltage(self):
        pass
    
    @abstractmethod
    def live(self):
        pass
    
    @abstractmethod
    def neutral(self):
        pass

    @abstractmethod
    def earth(self):
        pass

# Adaptee
# Define la interfaz existente que necesita adaptarse para
# aprovechar su funcionalidad especifica

class Socket(EuropeanSocketInterface):
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0

# Target interface
# Define la interface objetivo del dominio que usa el cliente

class USASocketInterface(ABC):
    @abstractmethod
    def voltage(self):
        pass

    @abstractmethod
    def live(self):
        pass

    @abstractmethod
    def neutral(self):
        pass

# Adapter
# Adapta la interfaz adaptee para usar en el objeto target
# Se observa que adapta a conveniencia solo el voltaje, sin
# embargo, como los otros dos valores no necesitan ser cambiados
# los mantiene.

class Adapter(USASocketInterface):
    _socket = None

    def __init__(self, socket):
        self._socket = socket

    def voltage(self):
        return 110
    
    def live(self):
        return self._socket.live()

    def neutral(self):
        return self._socket.neutral()

# Client
# Colabora con los objetos conformando la interface target

class Cafetera:
    _power = None

    def __init__(self, power):
        self._power = power

    def boil(self):

        if self._power.voltage() > 110:
            print("Se quema la cafetera!!")
        else:
            if self._power.live() == 1 and self._power.neutral() == -1:
                print("Es hora del cafe!")
            else:
                print("No hay energia")

def main():

    # Conectar

    # Adaptee
    socket = Socket()
    
    # Adapter
    adapter = Adapter(socket)

    # Client
    cafetera = Cafetera(adapter)

    # Hacer cafe
    cafetera.boil()

    return 0


if __name__ == "__main__":
    main()