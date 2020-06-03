from __future__ import annotations
from abc import ABC, abstractmethod
# Es un patro nde concepto que permite anadir nuevos comportamientos o caracteristicas
# a objetos dinamicamente poniendolos dentro de objetos especiales


# La interfaz base Component denie operaciones que pueden ser alteradas por decorators
class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# La clase ConcreteComponent implementa los metodos instanciados en la intefaz Component
class ConcreteComponent(Component):
    def operation(self) -> str:
        return "Concrete Component"

# El decorador base tambien ereda la misma interface que los otros componentes
# El principal proposito de esta clase es definir la interfaz contenedora para los 
# otros Concrete Component. La implementacion por default de el codigo contenedor
# deberia incluir un campo para guardar un Componente y tmb inicializarlo.

class Decorator(Component):
    _component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    # Aqui el decorador le delega todo el trabajo al Componente encapsulado
    @property
    def component(self) -> str:
        return self._component

    def operation(self) -> str:
        return self._component.operation()

# Los Concrete Decorators llaman el objeto encapsulado y altera su resultado en
# algun putno.

class ConcreteDecoratorA(Decorator):
    # Decorators pueden llamar la implementacion de operacion de su padre, en vez de llamar
    # directamente al objeto encapsulado. Esto simplifica la extension de la clase decorator.
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"

# Estos decorators tambien pueden ejecutar su operacion antes o despues de llamar al objeto encapsulado.
class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"

# El Cliente trabaja con todos los objetos usando la interface Component. Asi puede mantenerse
# desacoplado de los Concrete Component con los que trabaja.

def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}", end="")

if __name__ == "__main__":
    # Aqui el cliente soporta simples componentes
    simple = ConcreteComponent()
    print("Client: Tengo un componente simple")
    client_code(simple)
    print('\n')

    # Ahora los decorators
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Ahora tengo un componente decorado")
    client_code(decorator2)