from NodoTransaccionesConfig import NodoTrasaccionesConfig
class ListaTransaccionesConfig:
    def __init__(self) -> None:
        self.primero=NodoTrasaccionesConfig()
        self.ultimo=NodoTrasaccionesConfig()
        self.size=0

    def append(self, nuevatranconfig):
        if self.primero.idTransaccion is None:
            self.primero=nuevatranconfig
            self.ultimo=nuevatranconfig
            self.size += 1
        elif self.primero.siguiente is None:
            self.primero.siguiente=nuevatranconfig
            nuevatranconfig.anterior=self.primero
            self.ultimo=nuevatranconfig
            self.size += 1

        
        else:
            self.ultimo.siguiente=nuevatranconfig
            nuevatranconfig.anterior=self.ultimo
            self.ultimo=nuevatranconfig
            self.size += 1
    def bo(self):
        pass

        