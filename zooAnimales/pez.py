from zooAnimales.animal import Animal


class Pez(Animal):
	_listado = []
	salmones = 0
	bacalaos = 0

	def __init__(self,nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
		super().__init__(nombre, edad, habitat, genero)
		self._cantidadAletas = cantidadAletas
		self._colorEscamas = colorEscamas
		Pez._listado.append(self)

	def movimiento():
		return "nadar"

	@classmethod
	def crearSalmon(self,nombre,edad,genero):
		self.salmones+=1
		return Pez(nombre,edad,"oceano",genero,"rojo",6)

	@classmethod
	def crearBacalao(self,nombre,edad,genero):
		self.bacalaos+=1
		return Pez(nombre,edad,"oceano",genero,"gris",6)

	@classmethod
	def cantidadPeces(self):
		return len(self._listado)

	def getcantidadAletas(self):
		return self._cantidadAletas

	def setcantidadAletas(self,cantidadAletas):
		self._cantidadAletas = cantidadAletas

	def getcolorEscamas(self):
		return self._colorEscamas

	def setcolorEscamas(self,colorEscamas):
		self._colorEscamas = colorEscamas

	
	def getlistado(self):
		return self._listado

	
	def setlistado(self,listado):
		self._listado = listado