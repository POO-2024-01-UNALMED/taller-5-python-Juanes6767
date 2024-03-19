from zooAnimales.animal import Animal

class Ave(Animal):
    halcones=0
    aguilas=0
    listado=[]
    def __init__(self,nombre,edad,habitat,genero,colorPlumas):
        super.__init__(nombre,edad,habitat,genero)
        self._colorPlumas=colorPlumas