from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas=0
    serpientes=0
    listado=[]
    def __init__(self,nombre,edad,habitat,genero,colorEscamas,largoCola):
        super.__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._largoCola=largoCola

    