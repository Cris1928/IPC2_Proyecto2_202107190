
class NodoUlitmaTras:
    def __init__(self,idTransaccion=None,nombre=None,cantidad=None,tiempo=None):
        self.tiempo=tiempo
        self.nombre=nombre
        self.idTransaccion=idTransaccion
        self.cantidad=cantidad
        self.siguiente=None
        self.anterior=None
        