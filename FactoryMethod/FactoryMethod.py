from __future__ import annotations
#abd : Modulo Abstract Base Class
from abc import ABC, abstractmethod


class Creator(ABC):

    # La clase Creator declara el "factory method" que debe retornar un objeto
    # Producto. Las subclases de Creator implementan este metodo.

    @abstractmethod
    def factory_method(self):

        # Usualmente deberia haber una implementacion por defecto.
        pass

    def some_operation(self) -> str:

        # Las clases Creator no tienen como funcion principal crear productos, si no
        # operaciones (core business logic) con estos (obtenidos por el factory method).

        # Crea un objeto producto al llamar al factory method.
        product = self.factory_method()

        # Hacer algo con el producto
        result = f"Creator: El mismo codigo del creador, ha trabajado con el objeto:{product.operation()}"

        return result


# Las clases Concrete Creator sobrescriben el factory method con la finalidad de cambiar
# el producto resultante (tipo de producto). 

# Estos Concrete Creators son independientes de los Concrete Products con los que trabajen,
# mientras sigan referenciando a la interface Product.

class ConcreteCreator1(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):

    # La interface Product declara todas las operaciones que las clases Concrete Products
    # deben implementar

    @abstractmethod
    def operation(self) -> str:
        pass


# Las clases Concrete Products proveen varias implementaciones de la interface Product.

class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{ ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{ ConcreteProduct2}"


def client_code(creator: Creator) -> None:

    # El cliente trabaja con cualquier objeto de la clase Concrete Creator, mientras
    # que se siga referenciando la interface Creator, puede trabajar con cualquier
    # subclase de esta (Concrete Creator).

    print(f"Client: Yo no se con que clase de creador estoy trabajando, pero igual funciona.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())