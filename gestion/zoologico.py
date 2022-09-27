class Zoologico:
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    #getters and setters

    def getnombre(self): 
        return self._nombre

    def setnombre(self, nombre): 
        self._nombre = nombre

    def getubicacion(self,): 
        return self._ubicacion

    def setubicacion(self, ubicacion): 
        self._ubicacion = ubicacion

    def getzona(self): 
        return self._zonas

    def setzona(self, zonas): 
        self._zonas = zonas

    #metodos

    def agregarZonas(self, zona): 
        self._zonas.append(zona)
    
    def cantidadTotalAnimales(self): 
        return sum([i.cantidadAnimales() for i  in self._zonas])