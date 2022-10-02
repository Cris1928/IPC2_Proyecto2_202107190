#aquie hago un cambio de clientes
#ultimo cambio 
from NodoClientesDef import NodoListadoClientesD
class ListadoClientes:
    def __init__(self) -> None:
        self.primero=NodoListadoClientesD()
        self.ultimo=NodoListadoClientesD()
        self.size=0

    def append(self, nuevacliente):
        if self.primero.dpi is None:
            self.primero=nuevacliente
            self.ultimo=nuevacliente
            self.size += 1
        elif self.primero.siguiente is None:
            self.primero.siguiente=nuevacliente
            nuevacliente.anterior=self.primero
            self.ultimo=nuevacliente
            self.size += 1

        
        else:
            self.ultimo.siguiente=nuevacliente
            nuevacliente.anterior=self.ultimo
            self.ultimo=nuevacliente
            self.size += 1
    def buscarcliente(self,dpi):
        
        nodoaux=self.primero
        while nodoaux.dpi != dpi:
                if nodoaux.siguiente is not None:
                    nodoaux=nodoaux.siguiente
                else:
                    return None
        return nodoaux
    def print(self):
        nodoaux=self.primero
        cadena= ""
        num=1
        while True:
            if nodoaux.id is not None:
                cadena +=str(num)+". ("+str(nodoaux.nombre)+")"
                if nodoaux.siguiente is not None:
                    nodoaux=nodoaux.siguiente
                    cadena+="\n"
                    num=num+1
                else:
                    break
            else:
                break
        print(cadena)
    def calculo(self):
        actual=self.primero
        while actual is not None:
            print(actual.nombre)
            actual=actual.siguiente