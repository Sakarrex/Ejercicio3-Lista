import csv
from NodoLista import NodoLista

class ListaEncadenadaContenido:
    __cabeza = None
    __cantidad = None
    

    def __init__(self) -> None:
        self.__cabeza = None
        self.__cantidad = 0

        archivo = open("SuperficieIncendios.csv")
        reader = csv.reader(archivo,delimiter=";")
        cabecera = False
        provincia = ""
        hectareas = 0
        for line in reader:
            if cabecera == False:
                cabecera = True
                provincia = line[3]
                hectareas += float(line[6])
            else:
                if provincia != line[3]:
                    NuevoNodo = NodoLista(provincia,hectareas)
                    self.Insertar(NuevoNodo)
                    provincia = line[3]
                    hectareas = float(line[6])
                else:
                    hectareas += float(line[6])
                
                

        

    def Insertar(self,NuevoNodo):
        if self.__cabeza == None or self.__cabeza.getHectareas() < NuevoNodo.getHectareas():
            NuevoNodo.setSiguiente(self.__cabeza)
            self.__cabeza = NuevoNodo
        else:
            aux = self.__cabeza
            while aux.getSiguiente() != None and aux.getSiguiente().getHectareas() > NuevoNodo.getHectareas():
                aux = aux.getSiguiente()
            NuevoNodo.setSiguiente(aux.getSiguiente())
            aux.setSiguiente(NuevoNodo)
        



    def vacio(self):
        return self.__cabeza == None
    
    def Suprimir(self,posicion):
        if self.vacio():
            print("No se puede suprimir lista vacia")
        elif posicion < 0 or posicion >= self.__cantidad+1:
            print("Posicion no valida")
        else:
            aux = self.__cabeza
            actualPos = 1
            while actualPos < posicion-1:
                aux = aux.getSiguiente()
                actualPos += 1
            eliminar = aux.getSiguiente()
            aux.setSiguiente(eliminar.getSiguiente())
            del eliminar
            self.__cantidad -= 1
    
    def Buscar(self,elemento):
        encontrado = False
        aux = self.__cabeza
        while aux != None and encontrado == False:
            if aux.getValor() == elemento:
                encontrado = True
            aux = aux.getSiguiente()
        if not encontrado:
            print("Elemento no encontrado")
        else:
            print("Elemento encontrado")

    def Recorrer(self):
        aux = self.__cabeza
        while aux != None:
            print(aux)
            aux= aux.getSiguiente()

    def Primer_Elemento(self):
        return self.__cabeza.getValor()
    
    def Ultimo_Elemento(self):
        aux = self.__cabeza
        while aux.getSiguiente() != None:
            aux = aux.getSiguiente()
        return aux.getValor()
    
    def getAnterior(self,posicion):
        if not self.vacio() and posicion == 1:
            aux = self.__cabeza
            actualPos = 1
            while actualPos < posicion-1:
                aux = aux.getSiguiente()
                actualPos += 1
            return aux.getValor()
    
    def getSiguiente(self,posicion):
        if not self.vacio() and posicion < self.__cantidad:
            aux = self.__cabeza
            actualPos = 1
            while actualPos < posicion:
                aux = aux.getSiguiente()
                actualPos += 1
           
            return aux.getSiguiente().getValor()


