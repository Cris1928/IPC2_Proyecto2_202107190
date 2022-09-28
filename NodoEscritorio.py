class NodoEscritorio:
    def __init__(self,id=None,identificacion=None,encargado=None):
        self.id=id
        self.identificacion=identificacion
        self.encargado=encargado
        self.siguiente=None
        self.anterior=None