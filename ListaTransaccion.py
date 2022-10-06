#añado un metodo 
from NodoTransaccion import NodoTransaccion
class ListaTransaccion:
    def __init__(self) -> None:
        self.primero=NodoTransaccion()
        self.ultimo=NodoTransaccion()
        self.size=0
    def append(self, nuevaTransiccion):
        if self.primero.id is None:
            self.primero=nuevaTransiccion
            self.ultimo=nuevaTransiccion
            self.size += 1
        elif self.primero.siguiente is None:
            self.primero.siguiente=nuevaTransiccion
            nuevaTransiccion.anterior=self.primero
            self.ultimo=nuevaTransiccion
            self.size += 1
        else:
            self.ultimo.siguiente=nuevaTransiccion
            nuevaTransiccion.anterior=self.ultimo
            self.ultimo=nuevaTransiccion
            self.size += 1
    def buscarTrans(self,id):
        nodoaux=self.primero
        while nodoaux is not None:
            if nodoaux.id==id:
                return nodoaux
            else:
                n=nodoaux
             #   print(nodoaux.nombreTransaccion)
            nodoaux=nodoaux.siguiente
        return n

    def RetornTrans(self,id):
        nodoaux=self.primero
        while nodoaux.id != id:
                if nodoaux.siguiente is not None:
                 #   print(nodoaux.nombreTransaccion)
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
                cadena +=str(num)+". ("+str(nodoaux.nombreTransaccion)+")"
                if nodoaux.siguiente is not None:
                    nodoaux=nodoaux.siguiente
                    cadena+="\n"
                    num=num+1
                else:
                    break
            else:
                break
        print(cadena)