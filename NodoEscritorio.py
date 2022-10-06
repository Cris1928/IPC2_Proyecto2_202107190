#from ListadoClientes import ListadoClientes
from AtencionCliente import ListaAtencionCliente
#from ListaClientesDef import ListadoClientes
class NodoEscritorio:
    def __init__(self,id=None,identificacion=None,encargado=None,estado=None):
        self.id=id
        self.identificacion=identificacion
        self.encargado=encargado
        self.estado=estado
        self.listadoAtencionClientes=ListaAtencionCliente()
        self.siguiente=None
        self.anterior=None