from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# La clase Context define la interface usada por los clientes
class Context():

    def __init__(self, strategy : Strategy) -> None:
        # Usualmente, la  clase Context acepta una estrategia por el constructor
        # pero tambien provee un setter para cambiarlo durante la ejecucion.

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        # La clase Context mantiene una referencia a un objeto, que no conoce, de
        # la clase Strategy. Deberia poder funcionar con todas las estrategias por
        # medio de la interface Strategy.

        return self._strategy

    @strategy.setter
    def strategy(self, strategy : Strategy) -> None:
        # La clase Contexto permite remplazar el objeto vigente de la clase Strategy
        # en cualquier momento de la ejecucion.
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        # La clase Contexto delega un trabajo al objeto Strategy en vez de implementar
        # por su propia cuenta multiples versiones del algoritmo a implementar.

        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a","b","c","d","e"])
        print(",".join(result))

class Strategy(ABC):
    # La interface Strategy declara las operaciones comunes para todas las versiones de un
    # algoritmo a implementar.
    # La clase contexto usa esta interface para llamar al algoritmo definido en las clases
    # Concrete Strategies

    @abstractmethod
    def do_algorithm(self, data: List):
        pass

# Las clases Concrete Strategy implementan el algoritmo siguiendo la interface Strategy como base.
# La interface los hace intercambiables en el Contexto

class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data : List) -> List:
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def do_algorithm(self,data : List) -> List:
        return reversed(sorted(data))

if __name__ == "__main__":
    # El cliente escoge una estrategia concreta y la ejecuta por medio del contexto.
    # El cliente deberia estar al tanto de las diferencias entre las Concrete Strategies
    # para elegir la mejor opcion.

    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reverse sorting")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()