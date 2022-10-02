from NodoUltimaTrans import NodoUlitmaTras
class ListaTransaccionUlt:
    def __init__(self) -> None:
        self.primero=NodoUlitmaTras()
        self.ultimo=NodoUlitmaTras()
        self.size=0
    def append(self, nuevaTransiccion):
        if self.primero.idTransaccion is None:
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
    def mostrar(self):
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