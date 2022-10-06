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
    
    def tiempopromedio(self):
        actual=self.primero
        suma=0
        cantidad=0
        while actual is not None:
            suma+=(int(actual.tiempo))*(int(actual.cantidad))
            cantidad=cantidad+1
            actual=actual.siguiente
        if cantidad !=0:
            promedio=suma/cantidad
            return promedio
        else:
            return None
    def buscartrans(self,id):
        actual=self.primero
        while actual is not None:
            if actual.idTransaccion==id:
                return actual
            else:
                n=actual
            actual=actual.siguiente
        return n
