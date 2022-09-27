from zooAnimales.animal import Animal

class Mamifero(Animal):
	_listado = []
	caballos = 0
	leones = 0

    def __init__(self,nombre, edad, habitat, genero, pelaje, patas):
		super().__init__(nombre, edad, habitat, genero)
		self._pelaje = pelaje
		self._patas = patas
		Mamifero._listado.append(self)

	def getpelaje(self):
		return self._pelaje

	def setpelaje(self,pelaje):
		self._pelaje = pelaje

	def getpatas(self):
		return self._patas

	def setpatas(self,patas):
		self._patas = patas

	
	def getlistado(self):
		return Mamifero._listado

	
	def setlistado(self, listado):
		Mamifero._listado = listado


	@classmethod
	def crearCaballo(self,nombre,edad,genero):
		Mamifero.caballos+=1
		return Mamifero(nombre,edad,"pradera",genero,True,4)

	@classmethod
	def crearLeon(self,nombre,edad,genero):
		Mamifero.leones+=1
		return Mamifero(nombre,edad,"selva",genero,True,4)

	@classmethod
	def cantidadMamiferos(self):
		return len(Mamifero._listado)