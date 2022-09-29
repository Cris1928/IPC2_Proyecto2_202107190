from ListaTransaccionesConfig import ListaTransaccionesConfig
class NodoListadoClientes:
    def __init__(self,dpi=None,nombre=None):
        self.dpi=dpi
        self.nombre=nombre
        self.listaTransaccionesConfig=ListaTransaccionesConfig()
        self.siguiente=None
        self.anterior=None