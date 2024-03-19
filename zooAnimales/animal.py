from gestion.zona import Zona
from gestion.zoologico import Zoologico 
from .anfibio import Anfibio
from .ave import Ave
from .mamifero import Mamifero
from .pez import Pez
from .reptil import Reptil
from .animal import Animal
class Animal:
    totalAnimales=0
    def __init__(self,nombre,edad,habitat,genero):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=[]
        totalAnimales+=1


    def totalPorTipo():
        return "Mamiferos: "+len(Mamifero.getListado())+"\n"+"Aves: "+str(Ave.cantidadAves())+"\n"+"Reptiles: "+str(Reptil.cantidadReptiles())+"\n"+"Peces: "+str(Pez.cantidadPeces())+"\n"+"Anfibios: "+str(Anfibio.cantidadAnfibios())

    def toString(self):
        return ""+nombre+self._zona.nombre+Zona.getZoo().nombre

    def getNombre(self):
        return self._nombre
    
    def setNombre(self,nombre):
        self._nombre=nombre
    
    def getEdad(self):
        return self._edad
    
    def setEdad(self,edad):
        self._edad=edad
        
    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self,habitat):
        self._habitat=habitat
        
    def getGenero(self):
        return self._genero
    
    def setGenero(self,genero):
        self._genero=genero
        
    def getZona(self):
        return self._zona
    
    def setZona(self,zona):
        self._zona=zona