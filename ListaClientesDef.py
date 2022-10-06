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
        cont=1
        while actual is not None:
            print(str(cont)+". ("+str(actual.nombre)+")")
            cont=cont+1
            actual=actual.siguiente
    def tiempopromedioo(self):
        actual=self.primero
        suma=0
        while actual is not None:
            pass

    def tiempopromedio(self):
        actual=self.primero.listaTransacciones.primero
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
    def obtenerprimero(self):
        respuesta=self.primero
        self.primero=self.primero.siguiente
        return respuesta
    def buscarnombretrans(self,id):
        actual=self.primero.listaTransacciones.primero
        while actual is not None:
            if actual.idTransaccion==id:
                return actual
            else:
                n=actual
            actual=actual.siguiente
        return n