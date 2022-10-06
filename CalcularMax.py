class nodoMax:
    def __init__(self,num=None):
        self.num=num
        self.siguiente=None
        self.anterior=None
class ListMax:
    def __init__(self) -> None:
        self.primero=nodoMax()
        self.ultimo=nodoMax()
        self.size=0

    def append(self, nuevoPunto):
        if self.primero.num is None:
            self.primero=nuevoPunto
            self.ultimo=nuevoPunto
            self.size += 1
        elif self.primero.siguiente is None:
            self.primero.siguiente=nuevoPunto
            nuevoPunto.anterior=self.primero
            self.ultimo=nuevoPunto
            self.size += 1
        else:
            self.ultimo.siguiente=nuevoPunto
            nuevoPunto.anterior=self.ultimo
            self.ultimo=nuevoPunto
            self.size += 1
    def calcularMax(self):
        actual=self.primero
        au=0
        while actual is not None:
            if actual.num > au:

                au=actual.num
            else:
                pass
            actual=actual.siguiente

            
        return au
    
    def calcularProm(self):
        aux=0
        actual = self.primero
        suma=0
        while actual is not None:
            suma=suma+actual.num
            aux=aux+1
            actual=actual.siguiente
        if aux !=0:
            operacion=suma/aux
            return operacion
        else:
            return 0
    
    def calcularminimo(self):
        aux=self.calcularMax()
        actual=self.primero
        while actual is not None:
            
            actual=actual.siguiente