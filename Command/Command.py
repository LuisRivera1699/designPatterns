# Usado como alternativa a los callbacks methods de elementos UI
# Usado para encolar tareas, trackear un historial de operaciones, etc.

from __future__ import annotations
from abc import ABC, abstractmethod

# Esta interface declara un metodo para ejecutar un comando
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

# Esta clase implementa el metodo definido por su interface padre
class SimpleCommand(Command):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(
            f"SimpleCommand: Como un comando simple, puedo hacer cosas como imprimir"
            f"({self._payload})"
        )

# Al igual se pueden implementar hijos complejos que realicen operaciones complejas
# O recivan parametros referentes a otros objetos
class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, a:str, b:str) -> None:
        self._receiver = receiver
        self._a = a
        self._b = b
    
    def execute(self) -> None:
        print("ComplexCommand: Tareas complejas pueden ser hechas por el objeto Receiver", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


# Esta clase contiene la logica de negocio. Dentro de esta se realizan todas las operaciones
# asociadas al funcionamiento de la aplicacion, como procesar un request. Cualquier clase puede ser
# un receiver.

class Receiver:
    def do_something(self, a:str) -> None:
        print(f"\nReceiver: Estoy ({a}.)", end="")
    
    def do_something_else(self, b:str) -> None:
        print(f"\nReceiver: Tambien estoy ({b}.)", end="")


#Asociado con uno o mas Command. Envia una peticion de ejecutarse al Command.

class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command:Command):
        self._on_start = command

    def set_on_finish(self, command:Command):
        self._on_finish = command

    # Este invoker no depende de un command concreto o de las clases Receiver.
    # lo que hace el Invoker es pasar un reques a un Receiver indirectamente
    # ejecutando un Command.
    def do_something_important(self) -> None:
        print("Invoker: Alguien quiere hacer algo antes de que empiece?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...haciendo algo importante...")

        print("Invoker: Alguien quiere hacer algo dsp que acabe?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


# Ahora podemos simular el comportamiento del cliente

if __name__ == "__main__":
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Hola!"))
    receiver = Receiver()
    invoker.set_on_finish(
        ComplexCommand(
            receiver, "Enviando correo", "Guardando reporte"
        )
    )
    invoker.do_something_important()