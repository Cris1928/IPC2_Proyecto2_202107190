
from NodoPuntosAtencion import NodoPuntosAtencion
class ListaPuntosAntecnion:
    def __init__(self) -> None:
        self.primero=NodoPuntosAtencion()
        self.ultimo=NodoPuntosAtencion()
        self.size=0

    def append(self, nuevoPunto):
        if self.primero.id is None:
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
    def buscarescritorio(self,id):

        nodoaux=self.primero
        while nodoaux.id != id:
            if nodoaux.siguiente is not None:
                nodoaux=nodoaux.siguiente
            else:
                return None
     #   print(nodoaux.id)
        return nodoaux

    def printnuevo(self):



        nodoaux=self.primero
        cadena= ""
        num=1
        while True:

            if nodoaux.id is not None:



                cadena +=str(num)+". ("+str(nodoaux.nombrepuntoservicio)+")"
                if nodoaux.siguiente is not None:
                    nodoaux=nodoaux.siguiente
                    cadena+="\n"
                    num=num+1
                else:
                    break
            else:
                break
        print(cadena)





    def print(self):
        nodoaux=self.primero
        cadena= ""
        num=1
        while True:
            if nodoaux.id is not None and nodoaux.estado==1:
                cadena +=str(num)+". ("+str(nodoaux.nombrepuntoservicio)+")"
                if nodoaux.siguiente is not None:
                    nodoaux=nodoaux.siguiente
                    cadena+="\n"
                    num=num+1
                else:
                    break
            else:
                break
        print(cadena)

    def returnEvaluarEscritorio(self, numero):
            
        actual = self.primero
        i = 1
        
        while actual is not None:
            if actual.estado==1:
                if i == numero:
                    return actual.listaEsc
                else:
                    pass
                i += 1 
            else:
                pass
            actual = actual.siguiente  
    def returnEvaluarEscritorios(self, numero):
            
        actual = self.primero
        i = 1
        
        while actual is not None:
        
            if i == numero:
                return actual.listaEsc
            else:
                pass
            i += 1 
           
            actual = actual.siguiente   


    def returnEmpresa(self, numero):
            
        actual = self.primero
        i = 1
        
        while actual is not None:

        
            if i == numero:
                 #   returnpasciente = actual.ListaPuntosAtencion
                  #  return returnpasciente
                  actual.listaEsc.print()
                  
    
            actual = actual.siguiente
            i += 1        


    def CambiarEstado(self,ide):

 #       escAc=ListaEscritoriosActivos()
        actual=self.primero
        while actual is not None:

            if actual.id==ide:

                actual.estado=1
      #          print(actual.nombrepuntoservicio)
            else:
                pass
            actual=actual.siguiente
    def printEstado(self):
        nodoaux=self.primero
        cadena= ""
        num=1
        while nodoaux is not None:
            if nodoaux.estado == 1:
                cadena +=str(num)+". ("+str(nodoaux.nombrepuntoservicio)+")"
                cadena+="\n"
                num=num+1
            else:
                pass
            nodoaux=nodoaux.siguiente

        print(cadena)
    def calculo(self):
        actual=self.primero.listadoclientes.primero
        while actual is not None:
            print(actual.nombre)
            actual=actual.siguiente
    def cantidaddetrans(self):
        actual=self.primero.listadoclientes.primero.listaTransacciones.primero
        cont=0
        while actual is not None:
            cont=cont+1
            actual =actual.siguiente
        return(cont)



    def CantidaddeClientes(self):
        actual=self.primero.listadoclientes.primero
        contador=0
        while actual is not None:
            contador=contador+1
            #print(actual.nombre)
            actual=actual.siguiente
        return contador

    def EscritoriosInactivos(self):
        actual=self.primero.listaEsc.primero
        
