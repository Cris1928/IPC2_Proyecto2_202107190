from ListaPuntosAtencion import ListaPuntosAntecnion
from ListaTransaccion import ListaTransaccion

class NodoEmpresa:
    def __init__(self,id=None,nombre=None,abreviatura=None,estado=None):
        self.id=id
        self.nombre=nombre
        self.abreviatura=abreviatura
        self.estado=estado
        self.ListaPuntosAtencion=ListaPuntosAntecnion()
        self.ListaTransiccion=ListaTransaccion()
        self.siguiente=None