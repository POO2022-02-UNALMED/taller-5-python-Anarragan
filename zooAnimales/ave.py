from zooAnimales.animal import Animal

class Ave(Animal):

    _listado = []
    halcones = 0
    aguilas = 0


    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    def movimiento(self):
        return "volar"

    @classmethod
    def cantidadAves(self):
        return len(Ave._listado)

    @classmethod
    def crearHalcon(self, nombre, edad, genero):
        Ave.halcones+=1
        return Ave(nombre ,edad, "montanas", genero, "cafe glorioso")

    @classmethod
    def crearAguila(self, nombre, edad, genero):
        Ave.aguilas+=1
        return Ave(nombre, edad, "montanas", genero,"blanco y amarillo")

    def getcolorPlumas(self):
        return self._colorPlumas

    def setcolorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas

    def getlistado(self):
        return Ave._listado

    def setlistado(self, listado):
        Ave._listado = listado