from NodoConfiguracionInicial import NodoConfiguracionInicial
from ListaEmpresa import ListaEmpresa
class ListaConfiguracionInicial:
    def __init__(self) -> None:
        self.primero=NodoConfiguracionInicial()
        self.ultimo=NodoConfiguracionInicial()
        self.size=0


    def append(self, nuevaconfiguracion):
        if self.primero.id is None:
            self.primero=nuevaconfiguracion
            self.ultimo=nuevaconfiguracion
            self.size += 1
        elif self.primero.siguiente is None:
            self.primero.siguiente=nuevaconfiguracion
            nuevaconfiguracion.anterior=self.primero
            self.ultimo=nuevaconfiguracion
            self.size += 1

        
        else:
            self.ultimo.siguiente=nuevaconfiguracion
            nuevaconfiguracion.anterior=self.ultimo
            self.ultimo=nuevaconfiguracion
            self.size += 1
    def buscarconfig(self,id):
        
        nodoaux=self.primero
        while nodoaux.id != id:
                if nodoaux.siguiente is not None:
                    nodoaux=nodoaux.siguiente
                else:
                    return None
        return nodoaux
    def Configuracion(self,l):
        
        actual = l
        while actual is not None:
            print(actual.nombre)
            actual=actual.siguiente
        
