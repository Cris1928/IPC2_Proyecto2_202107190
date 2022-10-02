from NodoEscritoriosActivos import NodoEscritoriosActivos
class ListaEscritoriosActivos:
    def __init__(self) -> None:
        self.primero=NodoEscritoriosActivos()
        self.ultimo=NodoEscritoriosActivos()
        self.size=0
    def append(self, nuevoescritorioactivo):
        if self.primero.idEscritorioActivo is None:
            self.primero=nuevoescritorioactivo
            self.ultimo=nuevoescritorioactivo
            self.size += 1
        elif self.primero.siguiente is None:
            self.primero.siguiente=nuevoescritorioactivo
            nuevoescritorioactivo.anterior=self.primero
            self.ultimo=nuevoescritorioactivo
            self.size += 1

        
        else:
            self.ultimo.siguiente=nuevoescritorioactivo
            nuevoescritorioactivo.anterior=self.ultimo
            self.ultimo=nuevoescritorioactivo
            self.size += 1
