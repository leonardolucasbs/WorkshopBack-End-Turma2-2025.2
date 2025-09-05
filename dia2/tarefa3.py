
import math

class FiguraGeometrica:

    @staticmethod
    def calcCirculo(raio: float) -> float:
        return math.pi * math.pow(raio, 2)

    @staticmethod
    def calcTriangulo(base: float, altura: float) -> float:
        return (base * altura) / 2

    @staticmethod
    def calcHipotenusa(a: float, b: float) -> float:
        return math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    




    
