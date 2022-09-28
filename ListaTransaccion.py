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
