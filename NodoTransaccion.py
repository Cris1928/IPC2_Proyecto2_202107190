class NodoTransaccion:
    def __init__(self,id=None,nombreTransaccion=None,minutosAtencion=None):
        self.id=id
        self.nombreTransaccion=nombreTransaccion
        self.minutosAtencion=minutosAtencion
        self.siguiente=None
        self.anterior=None
        