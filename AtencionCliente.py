class NodoAtencionCliente:
    def __init__(self,dpi=None,nombre=None,tiempo=None):
        self.dpi=dpi
        self.nombre=nombre
        self.tiempo=tiempo
        self.siguiente=None
        self.anterior=None
class ListaAtencionCliente:
    def __init__(self) -> None:
        self.primero=NodoAtencionCliente()
        self.ultimo=NodoAtencionCliente()
        self.size=0
    def append(self, nuevacliente):
        if self.primero.dpi is None:
            self.primero=nuevacliente
            self.ultimo=nuevacliente
            self.size += 1
        elif self.primero.siguiente is None:
            self.primero.siguiente=nuevacliente
            nuevacliente.anterior=self.primero
            self.ultimo=nuevacliente
            self.size += 1
        else:
            self.ultimo.siguiente=nuevacliente
            nuevacliente.anterior=self.ultimo
            self.ultimo=nuevacliente
            self.size += 1
    def obtenerprimero(self):
        respuesta=self.primero
        self.primero=self.primero.siguiente
        return respuesta

    def p(self):
        actual=self
    def eliminardatos(self):
        if self.size>0:
            self.primero=None
            self.ultimo=None
            self.size=0
    def eliminar(self,id):
        actual=self.primero
        eliminado=False
        if actual is None:
            eliminado=False
        elif actual.dpi==id:
            self.primero=actual.siguiente
            self.primero.anterior=None
            eliminado=True
        elif self.ultimo.dpi==id:
            self.ultimo=self.ultimo.anterior
            self.ultimo.siguiente=None
            eliminado=True
        else:
            while actual:
                if actual.dpi==id:

                    actual.anterior.siguiente=actual.siguiente
                    actual.siguiente.anterior=actual.anterior
                    eliminado=True
                actual=actual.siguiente
        if eliminado:
            self.size-=1
        

    def mostrar(self):
        nodoaux=self.primero
        cadena= ""
        num=1
        while nodoaux is not None:
            if nodoaux.tiempo is not None:
                if int(nodoaux.tiempo) > 0:
                    cadena +=str(num)+". (NOMBRE: "+str(nodoaux.nombre)+")"+" (DPI: "+str(nodoaux.dpi)+")"+"  Atendiendo   "
                    cadena+="\n"
                    num=num+1
                elif int(nodoaux.tiempo) <= 0:
                    cadena +=str(num)+". (NOMBRE: "+str(nodoaux.nombre)+")"+" (DPI: "+str(nodoaux.dpi)+")"+"  Atendido   "
                    cadena+="\n"
                    num=num+1
                else:
                    pass
            else:
                pass
            nodoaux=nodoaux.siguiente

        print(cadena)
    
    