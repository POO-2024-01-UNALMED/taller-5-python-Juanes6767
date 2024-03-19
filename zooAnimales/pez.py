from zooAnimales.animal import Animal

class Pez(Animal):
    salmones=0
    bacalaos=0
    listado=[]
    def __init__(self,nombre,edad,habitat,genero,colorEscamas,cantidadAletas):
        super.__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._largoCola=cantidadAletas

