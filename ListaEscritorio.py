from NodoEscritorio import NodoEscritorio
class ListaEscritorio:
    def __init__(self) -> None:
        self.primero=NodoEscritorio()
        self.anterior=NodoEscritorio()
        self.size=0


    def append(self, nuevoescritorio):
        if self.primero.id is None:
            self.primero=nuevoescritorio
            self.ultimo=nuevoescritorio
            self.size += 1
        elif self.primero.siguiente is None:
            self.primero.siguiente=nuevoescritorio
            nuevoescritorio.anterior=self.primero
            self.ultimo=nuevoescritorio
            self.size += 1

        
        else:
            self.ultimo.siguiente=nuevoescritorio
            nuevoescritorio.anterior=self.ultimo
            self.ultimo=nuevoescritorio
            self.size += 1

