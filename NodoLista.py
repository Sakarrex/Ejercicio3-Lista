class NodoLista:
    __provincia = None
    __superficieTotal = None
    __siguiente = None
    

    def __init__(self,provincia = "",hectareas = 0) -> None:
        self.__provincia = provincia
        self.__superficieTotal = float(hectareas)
        self.__siguiente = None
    
    
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente
    
    def setProvincia(self,provincia):
        self.__provincia = provincia
    
    def setHectareas(self,hectareas):
        self.__superficieTotal = hectareas

    def getSiguiente(self):
        return self.__siguiente
    
    def getProvincia(self):
        return self.__provincia
    
    def getHectareas(self):
        return self.__superficieTotal
    
    def __str__(self) -> str:
        return "Provincia: {}, Hectareas: {}".format(self.__provincia,self.__superficieTotal)