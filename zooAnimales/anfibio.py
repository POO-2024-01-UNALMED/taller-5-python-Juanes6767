from zooAnimales.animal import Animal
class Anfibio(Animal):
    ranas=0
    salamandras=0
    listado=[]
    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        super.__init__(nombre,edad,habitat,genero)
        self._colorPiel=colorPiel
        self.venenoso=venenoso
    
    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self,colorPiel):
        self._colorPiel=colorPiel
    
    def getVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self,venenoso):
        self._venenoso=venenoso