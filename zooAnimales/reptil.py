from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas=0
    serpientes=0
    listado=[]
    def __init__(self,nombre,edad,habitat,genero,colorEscamas,largoCola):
        super.__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._largoCola=largoCola
    

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self,colorEscamas):
        self._colorEscamas=colorEscamas
    
    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self,largoCola):
        self._largoCola=largoCola

    