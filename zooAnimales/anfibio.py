from zooAnimales.animal import Animal
class Anfibio(Animal):
    ranas=0
    salamandras=0
    listado=[]
    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        super.__init__(nombre,edad,habitat,genero)
        self._colorPiel=colorPiel
        self.venenoso=venenoso