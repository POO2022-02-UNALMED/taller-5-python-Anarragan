class Zona:

    def __init__(self,nombre,zoo=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    #getters and setters

    def getnombre(self): 
        return self._nombre
        
    def setnombre(self, nombre): 
        self._nombre = nombre

    def getzoo(self): 
        return self._zoo

    def setzoo(self,zoo): 
        self._zoo = zoo

    def getanimales(self): 
        return self.animales

    def setanimales(self, animales): 
        self.animales = animales

    #metodos

    def agregarAnimales(self, animal): 
        self._animales.append(animal)
    
    def cantidadAnimales(self): 
        return len(self._animales)
