from __future__ import annotations
from abc import ABC, abstractmethod

# Es un patron estructuras que divide la logica de negocio por jerarquia de clases.
# A una de estas se le llama abstraction y a la segunda implementation.

# Define la interface para la parte de control de las dos jerarquias de clases.
# Mantiene una referencia a un objeto de la jerarquia implementation y delega todo
# el trabajo a este objeto
class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}"
            )

# Se puede extender la abstraccion sin cambiar la clase implementation
class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}"
            )

# La clase Implementation define la interface para todas las clases implementation.
# No tiene que hacer match con la interface Abstraction.
class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass

# Cada concrete implementation corresponde a una plataforma especifica e implementa
# la interface Implementation usando el api de la platarforma

class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Este es un resutado en la plataforma A"

class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Este es un resutado en la plataforma B"

# A excepcion de la fase de inicializacion, donde el objeto Abstraction es asociado con
# un objeto Implementation especifico, el Cliente deberia solo depender de la clase abstraccion.
# De esta manera el Cliente puede soportar cualquier combinacion Abstraction-Implementation

def client_code(abstraction: Abstraction) -> None:
    print(abstraction.operation(), end="")

# Este codigo de cliente debe poder trabajar con cualquier preconfiguracion Abstraction-Implementation

if __name__ == "__main__":
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print('\n')

    implementation = ConcreteImplementationB()
    abstraction = Abstraction(implementation)
    client_code(abstraction)