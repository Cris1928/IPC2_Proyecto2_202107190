#hice un cambio
#from ListaTransaccion import ListaTransaccion
from ListaUltTrans import ListaTransaccionUlt
class NodoListadoClientesD:
    def __init__(self,dpi=None,nombre=None,estado=None):
        self.estado=estado
        self.dpi=dpi
        self.nombre=nombre
        self.listaTransacciones=ListaTransaccionUlt()
        self.siguiente=None
        self.anterior=None