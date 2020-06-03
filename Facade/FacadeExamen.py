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

from __future__ import annotations
from abc import ABC, abstractmethod

class BarChart():
    def draw(self) -> None:
        print("He dibujado tu registro en un grafico de barras")

class PieChart():
    def draw(self) -> None:
        print("He dibujado tu registro en un grafico de pie")

# Movil Facade

class Facade():
    barChart = BarChart()
    pieChart = PieChart()

    def drawBarChart(self):
        self.barChart.draw()

    def drawPieChart(self):
        self.pieChart.draw()

class Cliente():
    facade = Facade()

    def barChartRegistroDeHoras(self):
        print("Quiero mi registro de horas en barchart ")
        self.facade.drawBarChart()

    def pieChartRegistroDeHoras(self):
        print("Quiero mi registro de horas en piechart ")
        self.facade.drawPieChart()
    


### Test

c = Cliente()

c.barChartRegistroDeHoras()
c.pieChartRegistroDeHoras()

## Log
#Quiero mi registro de horas en barchart
#He dibujado tu registro en un grafico de barras
#Quiero mi registro de horas en piechart
#He dibujado tu registro en un grafico de pie