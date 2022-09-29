
from NodoPuntosAtencion import NodoPuntosAtencion
class ListaPuntosAntecnion:
    def __init__(self) -> None:
        self.primero=NodoPuntosAtencion()
        self.ultimo=NodoPuntosAtencion()
        self.size=0

    def append(self, nuevoPunto):
        if self.primero.id is None:
            self.primero=nuevoPunto
            self.ultimo=nuevoPunto
            self.size += 1
        elif self.primero.siguiente is None:
            self.primero.siguiente=nuevoPunto
            nuevoPunto.anterior=self.primero
            self.ultimo=nuevoPunto
            self.size += 1
        else:
            self.ultimo.siguiente=nuevoPunto
            nuevoPunto.anterior=self.ultimo
            self.ultimo=nuevoPunto
            self.size += 1
    def buscarescritorio(self,id):

        nodoaux=self.primero
        while nodoaux.id != id:
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
                cadena +=str(num)+". ("+str(nodoaux.nombrepuntoservicio)+")"
                if nodoaux.siguiente is not None:
                    nodoaux=nodoaux.siguiente
                    cadena+="\n"
                    num=num+1
                else:
                    break
            else:
                break
        print(cadena)