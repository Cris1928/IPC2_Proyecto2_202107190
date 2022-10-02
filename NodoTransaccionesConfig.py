from email.errors import NonASCIILocalPartDefect


class NodoTrasaccionesConfig:
    def __init__(self,idTransaccion=None,cantidad=None):
        self.idTransaccion=idTransaccion
        self.cantidad=cantidad
        self.siguiente=None
        self.anterior=None
        