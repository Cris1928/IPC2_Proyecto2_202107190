#from ListadoClientes import ListadoClientes
class NodoEscritorio:
    def __init__(self,id=None,identificacion=None,encargado=None,estado=None):
        self.id=id
        self.identificacion=identificacion
        self.encargado=encargado
        self.estado=estado
     #   self.listadoClientes=ListadoClientes()
        self.siguiente=None
        self.anterior=None