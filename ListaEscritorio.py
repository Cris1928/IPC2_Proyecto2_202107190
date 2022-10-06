from re import I
from NodoEscritorio import NodoEscritorio
#from ListaEscritoriosActivos import ListaEscritoriosActivos
class ListaEscritorio:
    def __init__(self) -> None:
        self.primero=NodoEscritorio()
        self.anterior=NodoEscritorio()
        self.size=0


    def append(self, nuevoescritorio):
        if self.primero.id is None:
         #   print(self.primero.id)
            self.primero=nuevoescritorio
            self.ultimo=nuevoescritorio
            self.size += 1
        elif self.primero.siguiente is None:
            self.primero.siguiente=nuevoescritorio
            nuevoescritorio.anterior=self.primero
            self.ultimo=nuevoescritorio
            self.size += 1

        
        else:
            self.ultimo.siguiente=nuevoescritorio
            nuevoescritorio.anterior=self.ultimo
            self.ultimo=nuevoescritorio
            self.size += 1
    def vacio(self):
        pass
    def appendd(self,nuevoescritorio):
        if self.primero == None:
            self.primero=nuevoescritorio
            self.ultimo==nuevoescritorio
            self.size+=1
        else:
            self.primero.siguiente=self.primero
            self.primero=nuevoescritorio
            



    def CambiarEstados(self,ide):
 #       escAc=ListaEscritoriosActivos()
        actual=self.primero
        while actual is not None:
            if actual.id==ide:
                actual.estado=1
        #        print(actual.id)
            else:
                pass
          #      print(actual.id)

            actual=actual.siguiente


    def CambiarEstados2(self,ide):
 #       escAc=ListaEscritoriosActivos()
        actual=self.primero
        while actual is not None:
            if actual.id==ide:
                actual.estado=0
        #        print(actual.id)
            else:
                pass
          #      print(actual.id)

            actual=actual.siguiente



    def print(self):
        nodoaux=self.primero
        cadena= ""
        num=1
        while True:
            if nodoaux.id is not None and nodoaux.estado==1:
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
    def printt(self):
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
    def CantidaddeEstados(self):
        actual=self.primero
        contador=0
        while actual is not None:
            if actual.estado==1:
                contador=contador+1
            else:
                pass
            actual=actual.siguiente
        return contador
        
    def CantidaddeEstadosInactivos(self):
        actual=self.primero
        contador=0
        while actual is not None:
            if actual.estado==0:
                contador=contador+1
            else:
                pass
            actual=actual.siguiente
        return contador
    def Escritoriosinactivos(self):
        actual=self.primero
        cadena= ""
        num=1
        while actual is not None:
            if actual.estado==0:
                cadena +=str(num)+". ("+"id: "+str(actual.id)+" Estado: inactivo"+")"
                cadena+="\n"
                num=num+1
            else:
                pass
            actual=actual.siguiente
        print(cadena)


    def Escritoriosactivos(self):
        actual=self.primero
        cadena= ""
        num=1
        while actual is not None:
            if actual.estado==1:
                cadena +=str(num)+". ("+"id: "+str(actual.id)+" Estado: activo"+")"
                cadena+="\n"
                num=num+1
            else:
                pass
            actual=actual.siguiente
        print(cadena)

    def reevaluaresc(self, numero):
            
        actual = self.primero
        i = 1
        
        while actual is not None:
            if actual.estado==0:
                if i == numero:
                    self.eliminar(actual.id)
                    self.append(NodoEscritorio(actual.id,actual.identificacion,actual.identificacion,1))
                    #self.CambiarEstados(actual.id)
                else:
                    pass
                i += 1 
            else:
                pass
            actual = actual.siguiente  


    def reevaluaresc2(self, numero):
            
        actual = self.primero
        i = 1
        
        while actual is not None:
            if actual.estado==1:
                if i == numero:
                    self.eliminar(actual.id)
                    self.append(NodoEscritorio(actual.id,actual.identificacion,actual.identificacion,0))
                    
                    #self.CambiarEstados2(actual.id)
                else:
                    pass
                i += 1 
            else:
                pass
            actual = actual.siguiente 
    
    def eliminar(self,id):
        actual=self.primero
        eliminado=False
        if actual is None:
            eliminado=False
        elif actual.id==id:
            self.primero=actual.siguiente
            self.primero.anterior=None
            eliminado=True
        elif self.ultimo.id==id:
            self.ultimo=self.ultimo.anterior
            self.ultimo.siguiente=None
            eliminado=True
        else:
            while actual:
                if actual.id==id:
                    actual.anterior.siguiente=actual.siguiente
                    actual.siguiente.anterior=actual.anterior
                    eliminado=True
                actual=actual.siguiente
        if eliminado:
            self.size-=1


    def analizarescritorioenespera(self,tiempominimo):
        actual=self.primero
        while actual is not None:
            if actual.estado==2:
                actual.listadoAtencionClientes.primero.tiempo=int(actual.listadoAtencionClientes.primero.tiempo)-int(tiempominimo)
            else:
                pass
                


            actual=actual.siguiente
            
    def librarescritorio(self):
        actual=self.primero
        while actual is not None:
            a=actual.listadoAtencionClientes.primero.tiempo
            if a !=None:
                if int(a)<=0:
                    actual.estado=1
                    actual.listadoAtencionClientes.eliminardatos()
                else:
                    pass
            else:
                pass
            actual=actual.siguiente
