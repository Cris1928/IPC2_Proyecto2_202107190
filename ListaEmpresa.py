from NodoEmpresa import NodoEmpresa
class ListaEmpresa:
    def __init__(self) -> None:
        self.primero=NodoEmpresa()
        self.ultimo=NodoEmpresa()
        self.size=0
    def append(self,nuevaempresa):
        if self.primero.id is None:
            self.primero=nuevaempresa
            self.ultimo=nuevaempresa
            self.size += 1
        elif self.primero.siguiente is None:
            self.primero.siguiente=nuevaempresa
            self.ultimo=nuevaempresa
            self.size += 1
        else:

            self.ultimo.siguiente=nuevaempresa
            self.ultimo=nuevaempresa
            self.size += 1
    def print(self):
        nodoaux=self.primero
        cadena= ""
        num=1
        while True:
            if nodoaux.id is not None:
                cadena +=str(num)+". ("+str(nodoaux.id)+")"
                if nodoaux.siguiente is not None:
                    nodoaux=nodoaux.siguiente
                    cadena+="\n"
                    num=num+1
                else:
                    break
            else:
                break
        print(cadena)


    def buscarempresa(self,id):
        
        nodoaux=self.primero
        while nodoaux.id != id:
                if nodoaux.siguiente is not None:
                    nodoaux=nodoaux.siguiente
                else:
                    return None
        return nodoaux
