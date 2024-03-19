from zooAnimales.animal import Animal

class Mamifero(Animal):
    caballos=0
    leones=0
    listado=[]
    def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
        super.__init__(nombre,edad,habitat,genero)
        self._pelaje=pelaje
        self._patas=patas

    def getPelaje(self):
        return self._pelaje
    
    def setPelaje(self,pelaje):
        self._pelaje=pelaje
        
    def getPatas(self):
        return self._patas
    
    def setPatas(self,patas):
        self._patas=patas
    
    @classmethod
    def getListado(cls):
        return cls.listado