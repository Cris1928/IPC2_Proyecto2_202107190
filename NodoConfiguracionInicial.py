from ListaEscritoriosActivos import ListaEscritoriosActivos
from ListadoClientes import ListadoClientes
class NodoConfiguracionInicial:
    def __init__(self,id=None,idempresa=None,idputno=None):
        self.id=id
        self.idempresa=idempresa
        self.idpunto=idputno
        self.ListadoClientes=ListadoClientes()
        self.ListaEscritoriosActivos=ListaEscritoriosActivos()
        self.siguiente=None
        self.anterior=None

        