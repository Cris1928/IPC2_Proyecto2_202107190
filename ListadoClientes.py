from NodoListadoClientes import NodoListadoClientes
class ListadoClientes:
    def __init__(self) -> None:
        self.primero=NodoListadoClientes()
        self.ultimo=NodoListadoClientes()
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