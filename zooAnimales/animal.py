from gestion.zona import Zona

class Animal:

	_totalAnimales = 0

	def __init__(self,nombre, edad, habitat, genero, zona=None):
		self._nombre = nombre
		self._edad = edad
		self._habitat = habitat
		self._genero = genero
		self._zona = zona
		Animal._totalAnimales+=1

	def gethabitat(self):
		return self._habitat

	def sethabitat(self, habitat):
		self._habitat = habitat
        
    def getgenero(self):
		return self._genero
        
    def setgenero(self, genero):
		self._genero = genero

	def gettotalAnimales(self):
		return self._totalAnimales

	def getzona(self):
		return self._zona[0]

	def setzona(self, zona):
		self._zona[0] = zona

	def getnombre(self):
		return self._nombre

	def setnombre(self,nombre):
		self._nombre = nombre

	def getedad(self):
		return self._edad

	def setedad(self, edad):
		self._edad = edad


    def movimiento():
		return "desplazarse"

	@classmethod
	def totalPorTipo(self):
		from zooAnimales.anfibio import Anfibio
		from zooAnimales.reptil import Reptil
		from zooAnimales.mamifero import Mamifero
		from zooAnimales.ave import Ave
		from zooAnimales.pez import Pez

		return f"Mamiferos : {Mamifero.cantidadMamiferos()}\nAves : {Ave.cantidadAves()}\nReptiles : {Reptil.cantidadReptiles()}\nPeces : {Pez.cantidadPeces()}\nAnfibios : {Anfibio.cantidadAnfibios()}"

	def toString(self):
		if self._zona != None:
			return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona.getNombre()} en el {self._zona.getZoo().getNombre()}"
		else:
			return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"


